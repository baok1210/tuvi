"""
MingLi-Bench evaluation integration for Tử Vi Đẩu Số engine.

Evaluates our LLM integration + engine against 160 multiple-choice questions
from the Global Fortune Teller Competition (2022-2025).
"""

import json
import os
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Optional, Callable

BENCH_DATA_PATH = Path(__file__).parent.parent / "external" / "mingli-bench" / "data" / "data.json"
FORTUNE_DATA_PATH = Path(__file__).parent.parent / "external" / "mingli-bench" / "data" / "fortune_api_results.json"

CATEGORY_LABELS = {
    "婚姻": "Marriage", "事业": "Career", "家庭": "Family",
    "健康": "Health", "性格": "Personality", "财运": "Wealth",
    "学业": "Education", "子女": "Children", "外貌": "Appearance",
    "运势": "Fortune", "灾劫": "Calamity", "官非": "Legal",
}


@dataclass
class Question:
    id: str
    question_number: int
    case_id: str
    birth_info: dict
    question: str
    options: list
    answer: str
    category: str
    year: int = 0


@dataclass
class Result:
    question_id: str
    category: str
    year: int
    correct: bool
    predicted: Optional[str] = None
    answer: str = ""
    error: Optional[str] = None
    response_time: float = 0.0
    response: str = ""


def load_questions(years=None, categories=None, max_q=None):
    with open(BENCH_DATA_PATH, encoding="utf-8") as f:
        data = json.load(f)
    questions = []
    for q in data["questions"]:
        year = (q["question_number"] - 1) // 40 + 2022
        if years and year not in years:
            continue
        if categories and q.get("category") not in categories:
            continue
        questions.append(Question(
            id=q["id"], question_number=q["question_number"],
            case_id=q["case_id"], birth_info=q["birth_info"],
            question=q["question"], options=q["options"],
            answer=q["answer"], category=q.get("category", ""), year=year,
        ))
    if max_q:
        questions = questions[:max_q]
    return questions


def load_fortune_data():
    with open(FORTUNE_DATA_PATH, encoding="utf-8") as f:
        return json.load(f)


def build_prompt(q: Question, chart_context: str = "") -> str:
    bi = q.birth_info
    prompt = (
        f"以下是一道关于中国传统命理的题目。\n\n"
        f"命主信息：\n"
        f"性别：{'男' if bi['gender'] == '男' else '女'}\n"
        f"出生：{bi['year']}年{bi['month']}月{bi['day']}日 {bi['hour']}:{bi['minute']}\n"
        f"地点：{bi.get('country', bi.get('location', '未知'))}\n"
        f"历法：{bi.get('calendar_type', '公历')}"
    )
    if chart_context:
        prompt += f"\n\n紫微命盘：\n{chart_context}"
    prompt += f"\n\n问题：{q.question}\n\n选项：\n"
    for opt in q.options:
        prompt += f"{opt['letter']}. {opt['text']}\n"
    prompt += "\n请分析后给出答案，用'答案：X'的格式（X为A、B、C或D）。"
    return prompt


def build_prompt_vn(q: Question, chart_context: str = "") -> str:
    bi = q.birth_info
    prompt = (
        f"Bạn là chuyên gia Tử Vi Đẩu Số. Hãy trả lời câu hỏi trắc nghiệm sau.\n\n"
        f"THÔNG TIN LÁ SỐ:\n"
        f"Giới tính: {'Nam' if bi['gender'] == '男' else 'Nữ'}\n"
        f"Ngày sinh: {bi['year']}-{bi['month']}-{bi['day']} {bi['hour']}:{bi['minute']}\n"
        f"Quốc gia: {bi.get('country', bi.get('location', ''))}\n"
        f"Lịch: {bi.get('calendar_type', 'solar')}"
    )
    if chart_context:
        prompt += f"\n\nLÁ SỐ TỬ VI:\n{chart_context}"
    prompt += f"\n\nCÂU HỎI:\n{q.question}\n\nCÁC LỰA CHỌN:\n"
    for opt in q.options:
        prompt += f"{opt['letter']}. {opt['text']}\n"
    prompt += "\nHãy phân tích và chọn đáp án đúng. Kết thúc bằng: 答案：X"
    return prompt


def extract_answer(response: str) -> Optional[str]:
    response = response.strip()
    response = re.sub(r'[\*_`"\'"""''「」『』（）()[]【】<>《》,.。，]', ' ', response)

    patterns = [
        r'答案\s*[：:]\s*([A-D])',
        r'答案是\s*([A-D])',
        r'选择\s*([A-D])',
        r'选\s*([A-D])',
        r'^([A-D])\s*$',
    ]
    for p in patterns:
        matches = list(re.finditer(p, response, re.MULTILINE))
        if matches:
            return matches[-1].group(1).upper()

    letters = re.findall(r'\b([A-D])\b', response)
    return letters[-1].upper() if letters else None


def create_llm_fn(model="gpt-4o-mini", provider=None, base_url=None,
                  api_key=None, use_chart=False, temperature=0.0,
                  max_tokens=4096, lang="zh"):
    """Create an evaluation function that calls our LLM layer."""
    from knowledge.llm import ModelFactory
    client = ModelFactory.create(
        model=model, provider=provider, base_url=base_url,
        api_key=api_key, temperature=temperature, max_tokens=max_tokens,
    )

    chart_cache = {}
    if use_chart:
        chart_cache = _build_chart_cache()
        fortune_data = _load_fortune_map()

    def _call(q: Question) -> str:
        ctx = ""
        if use_chart and q.case_id in chart_cache:
            ctx = chart_cache[q.case_id]
        elif use_chart and q.case_id in fortune_data:
            ctx = _format_fortune_chart(fortune_data[q.case_id])
        prompt = build_prompt_vn(q, ctx) if lang == "vn" else build_prompt(q, ctx)
        return client.generate("", prompt)

    return _call


def create_direct_llm_fn(model="gpt-4o-mini", provider=None, base_url=None,
                         api_key=None, temperature=0.0, max_tokens=4096):
    """Create evaluation function that calls LLM directly without chart context."""
    return create_llm_fn(model, provider, base_url, api_key,
                         use_chart=False, temperature=temperature,
                         max_tokens=max_tokens)


def _load_fortune_map():
    data = load_fortune_data()
    return {item["case_id"]: item for item in data}


def _build_chart_cache():
    cache = {}
    fortune_map = _load_fortune_map()
    from tuvi_engine.pipeline import Layer1Algorithm
    l1 = Layer1Algorithm()
    for case_id, item in fortune_map.items():
        bi = item["birth_info"]
        try:
            ctx = l1.run(
                nam=int(bi["year"]),
                thang=int(bi["month"]),
                ngay=int(bi["day"]),
                gio=int(bi["hour"]),
                gioi_tinh="Nam" if bi.get("gender") == "男" else "Nữ",
            )
            cache[case_id] = l1.format_context(ctx)
        except Exception:
            cache[case_id] = _format_fortune_chart(item)
    return cache


def _format_fortune_chart(item: dict) -> str:
    ar = item.get("api_response", {})
    if not ar.get("data", {}).get("data"):
        return ""
    data = ar["data"]["data"]
    lines = [f"Mệnh: {data.get('soul','')} - Thân: {data.get('body','')}",
             f"Cục: {data.get('fiveElementsClass','')}",
             f"Ngày âm: {data.get('chineseDate','')}"]
    for p in data.get("palaces", []):
        majors = [s["name"] for s in p.get("majorStars", []) if s.get("name")]
        minors = [s["name"] for s in p.get("minorStars", []) if s.get("name")]
        all_s = majors + minors
        if all_s:
            lines.append(f"{p['name']}: {' '.join(all_s)}")
    return "\n".join(lines)


def evaluate(model_fn: Callable, years=None, categories=None,
             max_q=None, parallel=False, max_workers=5):
    questions = load_questions(years, categories, max_q)
    if parallel:
        return _evaluate_parallel(model_fn, questions, max_workers)
    return _evaluate_sequential(model_fn, questions)


def _evaluate_sequential(model_fn, questions):
    results = []
    for q in questions:
        start = time.time()
        try:
            response = model_fn(q)
            rt = time.time() - start
            predicted = extract_answer(response)
            results.append(Result(
                question_id=q.id, category=q.category, year=q.year,
                correct=predicted == q.answer, predicted=predicted,
                answer=q.answer, response_time=rt, response=response[:500],
            ))
        except Exception as e:
            results.append(Result(
                question_id=q.id, category=q.category, year=q.year,
                correct=False, error=str(e),
                response_time=time.time() - start,
            ))
    return _compute_stats(results), results


def _evaluate_parallel(model_fn, questions, max_workers):
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        fmap = {}
        for q in questions:
            start = time.time()
            future = ex.submit(_eval_one, model_fn, q, start)
            fmap[future] = q
        for future in as_completed(fmap):
            results.append(future.result())
    return _compute_stats(results), results


def _eval_one(model_fn, q, start_time):
    try:
        response = model_fn(q)
        rt = time.time() - start_time
        predicted = extract_answer(response)
        return Result(
            question_id=q.id, category=q.category, year=q.year,
            correct=predicted == q.answer, predicted=predicted,
            answer=q.answer, response_time=rt, response=response[:500],
        )
    except Exception as e:
        return Result(
            question_id=q.id, category=q.category, year=q.year,
            correct=False, error=str(e),
            response_time=time.time() - start_time,
        )


def _compute_stats(results):
    total = len(results)
    correct = sum(1 for r in results if r.correct)
    errors = sum(1 for r in results if r.error)

    by_cat = {}
    for r in results:
        by_cat.setdefault(r.category, {"total": 0, "correct": 0, "label": CATEGORY_LABELS.get(r.category, r.category)})
        by_cat[r.category]["total"] += 1
        if r.correct:
            by_cat[r.category]["correct"] += 1

    for v in by_cat.values():
        v["accuracy"] = v["correct"] / v["total"] if v["total"] else 0

    by_year = {}
    for r in results:
        by_year.setdefault(r.year, {"total": 0, "correct": 0})
        by_year[r.year]["total"] += 1
        if r.correct:
            by_year[r.year]["correct"] += 1

    avg_rt = sum(r.response_time for r in results) / total if total else 0

    return {
        "total": total,
        "correct": correct,
        "accuracy": correct / total if total else 0,
        "errors": errors,
        "by_category": by_cat,
        "by_year": by_year,
        "avg_response_time": avg_rt,
        "results": [(r.question_id, r.category, r.correct, r.predicted, r.answer) for r in results],
    }


def print_report(stats: dict):
    print("=" * 55)
    print(f"  MingLi-Bench Evaluation Report")
    print("=" * 55)
    print(f"  Tổng số:        {stats['total']}")
    print(f"  Đúng:           {stats['correct']}")
    print(f"  Độ chính xác:   {stats['accuracy']:.2%}")
    print(f"  Lỗi:            {stats['errors']}")
    print(f"  Thời gian TB:   {stats['avg_response_time']:.2f}s")
    print()
    print(f"  {'Danh mục':<14s} {'SL':>4s} {'Đúng':>4s} {'Acc':>8s}")
    print("  " + "-" * 32)
    for cat, v in sorted(stats["by_category"].items(), key=lambda x: -x[1]["accuracy"]):
        print(f"  {v['label']:<14s} {v['total']:4d} {v['correct']:4d} {v['accuracy']:7.1%}")
    print()
    print(f"  {'Năm':<6s} {'SL':>4s} {'Đúng':>4s} {'Acc':>8s}")
    print("  " + "-" * 24)
    for yr, v in sorted(stats["by_year"].items()):
        acc = v["correct"] / v["total"] if v["total"] else 0
        print(f"  {yr:<6d} {v['total']:4d} {v['correct']:4d} {acc:7.1%}")


def dataset_stats():
    """Print dataset statistics."""
    questions = load_questions()
    by_cat = {}
    for q in questions:
        by_cat[q.category] = by_cat.get(q.category, 0) + 1
    by_year = {}
    for q in questions:
        by_year[q.year] = by_year.get(q.year, 0) + 1

    print(f"Dataset MingLi-Bench: {len(questions)} câu hỏi")
    print(f"Cases: {len(set(q.case_id for q in questions))}")
    print(f"\nPhân bố năm: {', '.join(f'{y}: {c}' for y, c in sorted(by_year.items()))}")
    print(f"\nPhân bố danh mục:")
    for cat, cnt in sorted(by_cat.items(), key=lambda x: -x[1]):
        label = CATEGORY_LABELS.get(cat, cat)
        print(f"  {cat} ({label}): {cnt}")

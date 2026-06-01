import json
import os
from collections import Counter

BENCH_PATH = os.path.join(os.path.dirname(__file__), "..", "external", "mingli-bench", "data", "data.json")

CATEGORY_LABELS = {
    "婚姻": "Marriage", "事业": "Career", "家庭": "Family",
    "健康": "Health", "性格": "Personality", "财运": "Wealth",
    "学业": "Education", "子女": "Children", "外貌": "Appearance",
    "运势": "Fortune", "灾劫": "Calamity", "官非": "Legal",
}


def load_benchmark():
    with open(BENCH_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return data["questions"]


def stats():
    questions = load_benchmark()
    cat_count = Counter(q["category"] for q in questions)
    print(f"Tong: {len(questions)} cau hoi")
    print(f"Phan bo:")
    for cat, count in sorted(cat_count.items(), key=lambda x: -x[1]):
        label = CATEGORY_LABELS.get(cat, cat)
        print(f"  {cat} ({label}): {count}")
    print(f"\nSo case: {len(set(q['case_id'] for q in questions))}")
    print(f"Nam: 2022-2025 (40 cau/nam)")


def evaluate_model(model_fn, years=None, categories=None):
    questions = load_benchmark()
    if years:
        questions = [q for q in questions if q["question_number"] // 40 + 2022 - (0 if q["question_number"] % 40 else 1) in years]
    if categories:
        questions = [q for q in questions if q["category"] in categories]

    correct = 0
    results = []
    for q in questions:
        predicted = model_fn(q)
        is_correct = predicted == q["answer"]
        if is_correct:
            correct += 1
        results.append({
            "id": q["id"],
            "category": q["category"],
            "correct": is_correct,
            "predicted": predicted,
            "answer": q["answer"],
        })

    accuracy = correct / len(questions) if questions else 0
    return {
        "accuracy": accuracy,
        "correct": correct,
        "total": len(questions),
        "results": results,
    }


def evaluate_from_file(predictions_file):
    with open(BENCH_PATH, encoding="utf-8") as f:
        questions = {q["id"]: q for q in json.load(f)["questions"]}
    with open(predictions_file, encoding="utf-8") as f:
        predictions = json.load(f)

    correct = 0
    for pred in predictions:
        qid = pred["id"]
        if qid in questions and pred.get("answer") == questions[qid]["answer"]:
            correct += 1

    return {
        "accuracy": correct / len(predictions),
        "correct": correct,
        "total": len(predictions),
    }


def format_birth_info(q):
    bi = q["birth_info"]
    return {
        "gender": "Nam" if bi["gender"] == "男" else "Nữ",
        "year": bi["year"],
        "month": bi["month"],
        "day": bi["day"],
        "hour": bi["hour"],
        "minute": bi["minute"],
        "country": bi.get("country", ""),
    }


if __name__ == "__main__":
    stats()

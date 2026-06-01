import json
import os
import hashlib
import time
from typing import Optional

CACHE_DIR = os.path.join(os.path.dirname(__file__), "..", "..", ".llm_cache")
CACHE_TTL = 3600


class LLMCache:
    def __init__(self, ttl: int = CACHE_TTL):
        self.ttl = ttl
        os.makedirs(CACHE_DIR, exist_ok=True)

    def _make_key(self, chart_json: str, model: str, prompt: str) -> str:
        raw = f"{chart_json}:{model}:{prompt}"
        return hashlib.md5(raw.encode()).hexdigest()

    def get(self, chart_json: str, model: str, prompt: str) -> Optional[str]:
        key = self._make_key(chart_json, model, prompt)
        path = os.path.join(CACHE_DIR, f"{key}.json")
        if not os.path.exists(path):
            return None
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if time.time() - data["ts"] > self.ttl:
                os.remove(path)
                return None
            return data["result"]
        except (json.JSONDecodeError, KeyError, OSError):
            return None

    def set(self, chart_json: str, model: str, prompt: str, result: str):
        key = self._make_key(chart_json, model, prompt)
        path = os.path.join(CACHE_DIR, f"{key}.json")
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump({"ts": time.time(), "result": result}, f, ensure_ascii=False)
        except OSError:
            pass

    def clear(self, older_than: Optional[int] = None):
        if not os.path.exists(CACHE_DIR):
            return
        now = time.time()
        for fname in os.listdir(CACHE_DIR):
            fpath = os.path.join(CACHE_DIR, fname)
            if not fname.endswith(".json"):
                continue
            try:
                mtime = os.path.getmtime(fpath)
                if (older_than and now - mtime > older_than) or (not older_than):
                    os.remove(fpath)
            except OSError:
                pass

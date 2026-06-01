import os
from typing import Optional, Dict
from dotenv import load_dotenv

load_dotenv()

PROVIDER_CONFIGS: Dict[str, Dict[str, Optional[str]]] = {
    "openai": {
        "api_key_env": "OPENAI_API_KEY",
        "base_url_env": "OPENAI_BASE_URL",
        "default_base_url": "https://api.openai.com/v1",
    },
    "anthropic": {
        "api_key_env": "ANTHROPIC_API_KEY",
        "base_url_env": "ANTHROPIC_BASE_URL",
        "default_base_url": "https://api.anthropic.com",
    },
    "deepseek": {
        "api_key_env": "DEEPSEEK_API_KEY",
        "base_url_env": "DEEPSEEK_BASE_URL",
        "default_base_url": "https://api.deepseek.com",
    },
    "openrouter": {
        "api_key_env": "OPENROUTER_API_KEY",
        "base_url_env": "OPENROUTER_BASE_URL",
        "default_base_url": "https://openrouter.ai/api/v1",
    },
    "groq": {
        "api_key_env": "GROQ_API_KEY",
        "base_url_env": "GROQ_BASE_URL",
        "default_base_url": "https://api.groq.com/openai/v1",
    },
    "custom1": {
        "api_key_env": "CUSTOM1_API_KEY",
        "base_url_env": "CUSTOM1_BASE_URL",
        "default_base_url": None,
    },
    "custom2": {
        "api_key_env": "CUSTOM2_API_KEY",
        "base_url_env": "CUSTOM2_BASE_URL",
        "default_base_url": None,
    },
    "custom3": {
        "api_key_env": "CUSTOM3_API_KEY",
        "base_url_env": "CUSTOM3_BASE_URL",
        "default_base_url": None,
    },
}


def get_provider_config(provider: str) -> Optional[Dict[str, Optional[str]]]:
    return PROVIDER_CONFIGS.get(provider)


def resolve_provider_from_model(model: str) -> str:
    CUSTOM_PREFIXES = {"custom1", "custom2", "custom3"}
    if "/" in model:
        prefix = model.split("/")[0].lower()
        if prefix in CUSTOM_PREFIXES:
            return prefix
        return "openrouter"
    if model.startswith("gpt-") or model.startswith("o1-") or model.startswith("o3-") or model.startswith("o4-"):
        return "openai"
    if model.startswith("claude-"):
        return "anthropic"
    if model.startswith("deepseek-"):
        return "deepseek"
    return "openai"


class LLMConfig:
    def __init__(self, model: str, provider: Optional[str] = None,
                 base_url: Optional[str] = None, api_key: Optional[str] = None,
                 temperature: float = 0.7, max_tokens: int = 4096):
        self.model = model
        self.provider = provider or resolve_provider_from_model(model)
        self.base_url = base_url
        self.api_key = api_key
        self.temperature = temperature
        self.max_tokens = max_tokens
        self._resolve()

    def _resolve(self):
        pconf = get_provider_config(self.provider)
        if not self.api_key and pconf:
            self.api_key = os.getenv(pconf["api_key_env"], "")
        if not self.base_url:
            if pconf and pconf["base_url_env"]:
                self.base_url = os.getenv(pconf["base_url_env"]) or pconf["default_base_url"]
            elif pconf:
                self.base_url = pconf["default_base_url"]

    def uses_openai_compat(self) -> bool:
        openai_compat_providers = {"openai", "deepseek", "openrouter", "groq",
                                    "custom1", "custom2", "custom3"}
        return self.provider in openai_compat_providers

    def to_dict(self) -> dict:
        return {
            "model": self.model,
            "provider": self.provider,
            "base_url": self.base_url,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }

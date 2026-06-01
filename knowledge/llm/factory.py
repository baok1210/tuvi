from typing import Optional
from .base import BaseLLMClient
from .config import LLMConfig
from .openai_compat import OpenAICompatibleClient
from .anthropic import AnthropicClient


class ModelFactory:
    _registry = {
        "openai_compat": OpenAICompatibleClient,
        "anthropic": AnthropicClient,
    }

    @classmethod
    def register(cls, name: str, client_class):
        cls._registry[name] = client_class

    @classmethod
    def create(cls, model: str, provider: Optional[str] = None,
               base_url: Optional[str] = None, api_key: Optional[str] = None,
               temperature: float = 0.7, max_tokens: int = 4096) -> BaseLLMClient:
        cfg = LLMConfig(model, provider, base_url, api_key, temperature, max_tokens)

        if cfg.uses_openai_compat():
            client_cls = cls._registry["openai_compat"]
        elif cfg.provider == "anthropic":
            client_cls = cls._registry["anthropic"]
        else:
            client_cls = cls._registry["openai_compat"]

        return client_cls(
            model_name=cfg.model,
            api_key=cfg.api_key,
            base_url=cfg.base_url,
            temperature=cfg.temperature,
            max_tokens=cfg.max_tokens,
        )

    @classmethod
    def list_supported_models(cls) -> dict:
        return {
            "openai": ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo", "o1-mini"],
            "anthropic": ["claude-3-5-sonnet-latest", "claude-3-5-haiku-latest"],
            "deepseek": ["deepseek-chat", "deepseek-reasoner"],
            "openrouter": ["openai/gpt-4o", "anthropic/claude-3.5-sonnet",
                           "google/gemini-2.0-flash", "deepseek/deepseek-r1"],
            "groq": ["groq/llama-3.3-70b", "groq/mixtral-8x7b"],
            "custom1": ["custom1/<your-model>"],
            "custom2": ["custom2/<your-model>"],
            "custom3": ["custom3/<your-model>"],
        }

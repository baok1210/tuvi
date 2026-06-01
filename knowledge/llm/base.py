from abc import ABC, abstractmethod
from typing import Optional, AsyncGenerator


class BaseLLMClient(ABC):
    def __init__(self, model_name: str, api_key: Optional[str] = None,
                 base_url: Optional[str] = None, temperature: float = 0.7,
                 max_tokens: int = 4096):
        self.model_name = model_name
        self.api_key = api_key
        self.base_url = base_url
        self.temperature = temperature
        self.max_tokens = max_tokens

    @abstractmethod
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        ...

    @abstractmethod
    async def generate_stream(self, system_prompt: str, user_prompt: str) -> AsyncGenerator[str, None]:
        ...
        yield ""

    @abstractmethod
    def count_tokens(self, text: str) -> int:
        ...

    def get_meta(self) -> dict:
        return {
            "model": self.model_name,
            "provider": self.__class__.__name__,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }

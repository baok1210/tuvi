from typing import Optional, AsyncGenerator
from anthropic import Anthropic, AsyncAnthropic, APIError, RateLimitError
from .base import BaseLLMClient


class AnthropicClient(BaseLLMClient):
    def __init__(self, model_name: str, api_key: Optional[str] = None,
                 base_url: Optional[str] = None, temperature: float = 0.7,
                 max_tokens: int = 4096, max_retries: int = 3):
        super().__init__(model_name, api_key, base_url, temperature, max_tokens)
        kwargs = {
            "api_key": self.api_key,
            "max_retries": max_retries,
        }
        if self.base_url:
            kwargs["base_url"] = self.base_url
        self._client = Anthropic(**kwargs)
        self._async_client = AsyncAnthropic(**kwargs)

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        try:
            resp = self._client.messages.create(
                model=self.model_name,
                system=system_prompt,
                messages=[{"role": "user", "content": user_prompt}],
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )
            return resp.content[0].text if resp.content else ""
        except RateLimitError as e:
            raise RuntimeError(f"Rate limited: {e}")
        except APIError as e:
            raise RuntimeError(f"API error: {e}")

    async def generate_stream(self, system_prompt: str, user_prompt: str) -> AsyncGenerator[str, None]:
        async with self._async_client.messages.stream(
            model=self.model_name,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        ) as stream:
            async for text in stream.text_stream:
                yield text

    def count_tokens(self, text: str) -> int:
        return len(text) // 4

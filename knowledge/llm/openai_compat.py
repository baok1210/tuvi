import json
from typing import Optional, AsyncGenerator
from openai import OpenAI, AsyncOpenAI, APIError, RateLimitError
from .base import BaseLLMClient


class OpenAICompatibleClient(BaseLLMClient):
    def __init__(self, model_name: str, api_key: Optional[str] = None,
                 base_url: Optional[str] = None, temperature: float = 0.7,
                 max_tokens: int = 4096, max_retries: int = 3):
        super().__init__(model_name, api_key, base_url, temperature, max_tokens)
        self._client = OpenAI(
            api_key=self.api_key or "not-needed",
            base_url=self.base_url,
            max_retries=max_retries,
        )
        self._async_client = AsyncOpenAI(
            api_key=self.api_key or "not-needed",
            base_url=self.base_url,
            max_retries=max_retries,
        )

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        try:
            resp = self._client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )
            return resp.choices[0].message.content or ""
        except RateLimitError as e:
            raise RuntimeError(f"Rate limited: {e}")
        except APIError as e:
            raise RuntimeError(f"API error: {e}")

    async def generate_stream(self, system_prompt: str, user_prompt: str) -> AsyncGenerator[str, None]:
        stream = await self._async_client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            stream=True,
        )
        async for chunk in stream:
            delta = chunk.choices[0].delta if chunk.choices else None
            if delta and delta.content:
                yield delta.content

    def count_tokens(self, text: str) -> int:
        return len(text) // 4

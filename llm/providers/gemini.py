from typing import AsyncIterator, override

from .base import LLMChunk, LLMProvider, LLMResponse


class GeminiProvider(LLMProvider):
    """Google Gemini provider."""

    @override
    async def generate(self, prompt: str, **kwargs) -> LLMResponse:
        """Generate full response from Gemini (non-streaming)."""
        raise NotImplementedError

    @override
    async def generate_stream(self, prompt: str, **kwargs) -> AsyncIterator[LLMChunk]:
        """Stream Gemini response as async iterator of LLMChunk."""
        raise NotImplementedError
        yield

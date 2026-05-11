from typing import AsyncIterator, override

from .base import LLMChunk, LLMProvider, LLMResponse


class AzureProvider(LLMProvider):
    """Async Azure OpenAI provider"""

    @override
    async def generate(self, prompt: str, **kwargs) -> LLMResponse:
        """Generate full response from Azure OpenAI (non-streaming)."""
        raise NotImplementedError

    @override
    async def generate_stream(self, prompt: str, **kwargs) -> AsyncIterator[LLMChunk]:
        """Stream Azure OpenAI response as async iterator of LLMChunk."""
        raise NotImplementedError
        yield

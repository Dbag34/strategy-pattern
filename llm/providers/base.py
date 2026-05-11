from abc import ABC, abstractmethod
from typing import AsyncIterator

from ..config import LLMConfig
from ..types import LLMChunk, LLMResponse


class LLMProvider(ABC):
    """Abstract base for all async LLM providers."""

    def __init__(self, config: LLMConfig):
        self.name = config.name
        self.stream = config.stream
        self.config = config

    @abstractmethod
    async def generate(self, prompt: str, **kwargs) -> LLMResponse:
        """Non-streaming: return complete LLMResponse. Raise on failure."""
        ...

    @abstractmethod
    def generate_stream(self, prompt: str, **kwargs) -> AsyncIterator[LLMChunk]:
        """Streaming: yield LLMChunk deltas. Raise on failure."""
        ...

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} name={self.name!r} stream={self.stream}>"

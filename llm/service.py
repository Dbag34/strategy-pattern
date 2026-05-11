import logging
from typing import AsyncIterator

from .config import Config
from .exceptions import AllProvidersFailedError
from .providers import LLMProvider
from .registry import PROVIDER_REGISTRY
from .types import LLMChunk, LLMResponse

logger = logging.getLogger(__name__)


class LLMService:
    """LLM service with ordered fallback."""

    def __init__(self, config: Config):
        self._providers: list[LLMProvider] = self._build_providers(config)

    async def generate(self, prompt: str, **kwargs) -> LLMResponse:
        """Try each non-streaming provider in order. Returns the first successful LLMResponse."""

        for provider in self._providers:
            if provider.stream:
                continue
            try:
                logger.info("Trying provider (non-stream): %s", provider.name)
                response = await provider.generate(prompt, **kwargs)
                logger.info("Success: %s", provider.name)
                return response
            except Exception as exc:
                logger.warning("Provider %s failed: %s", provider.name, exc)

        raise AllProvidersFailedError()

    async def stream(self, prompt: str, **kwargs) -> AsyncIterator[LLMChunk]:
        """Try each streaming provider in order. Yields chunks from the first one that succeeds."""

        for provider in self._providers:
            if not provider.stream:
                continue
            try:
                logger.info(f"Trying provider (stream): {provider.name}")
                async for chunk in provider.generate_stream(prompt, **kwargs):
                    yield chunk
                return
            except Exception as exc:
                logger.exception(f"Provider {provider.name} failed: {exc}")

        raise AllProvidersFailedError()

    def _build_providers(self, config: Config) -> list[LLMProvider]:
        """Builds registry for tenant specific LLMs"""

        providers = []
        for entry in config.llms:
            provider_type = entry.type
            cls = PROVIDER_REGISTRY.get(provider_type)

            if cls is None:
                raise ValueError(
                    f"Unknown provider type {provider_type!r}. "
                    f"Available: {list(PROVIDER_REGISTRY)}"
                )
            providers.append(cls(entry))
        if not providers:
            raise ValueError("Config must define at least one LLM under 'llms'.")
        return providers

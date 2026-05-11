from .enums import ProviderType
from .providers import AzureProvider, GeminiProvider, LLMProvider

PROVIDER_REGISTRY: dict[str, type[LLMProvider]] = {
    ProviderType.AZURE: AzureProvider,
    ProviderType.GEMINI: GeminiProvider,
    
}

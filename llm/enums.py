from enum import Enum


class ProviderType(str, Enum):
    AZURE = "azure"
    GEMINI = "gemini"

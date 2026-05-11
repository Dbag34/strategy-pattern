from enum import Enum

from pydantic import BaseModel


class ProviderType(str, Enum):
    AZURE = "azure"
    GEMINI = "gemini"

class ExperimentMode(int, Enum):
    A = 1
    B = 2

class ProviderConfig(BaseModel):
    type: ProviderType
    name: str
    api_key: str


ProviderConfig(type=ProviderType.AZURE, name="azure-primary", api_key="sk-xxx")


print(ProviderType.AZURE == "azure")

print(ExperimentMode.A == 1)
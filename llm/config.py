from typing import Annotated, List, Literal

from pydantic import BaseModel, Field, SecretStr

from .enums import ProviderType


class AzureLLM(BaseModel):
    name: str
    type: Literal[ProviderType.AZURE]
    stream: bool = True
    api_key: SecretStr
    endpoint: str
    deployment: str
    api_version: str


class GeminiLLM(BaseModel):
    name: str
    type: Literal[ProviderType.GEMINI]
    stream: bool = True
    api_key: SecretStr
    model: str


type LLMConfig = Annotated[AzureLLM | GeminiLLM, Field(discriminator="type")]


class Config(BaseModel):
    llms: List[LLMConfig]

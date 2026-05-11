from typing import Any

from pydantic import BaseModel, Field


class LLMResponse(BaseModel):
    text: str
    provider: str
    model: str
    usage: dict[str, int] = Field(default_factory=dict)
    raw: Any = None


class LLMChunk(BaseModel):
    delta: str
    provider: str
    model: str
    is_final: bool = False

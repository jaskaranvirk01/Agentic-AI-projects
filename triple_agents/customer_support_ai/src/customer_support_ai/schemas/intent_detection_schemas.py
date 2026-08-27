from pydantic import BaseModel, Field


class IntentOutput(BaseModel):
    intent: str
    intent_confidence: float = Field(ge=0.0, le=1.0)

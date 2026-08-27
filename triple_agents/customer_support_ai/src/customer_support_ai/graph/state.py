from typing import TypedDict


class SupportState(TypedDict):
    user_query: str | None
    intent: str | None
    intent_confidence: float | None
    retrieved_documents: list | None
    response: str | None

from pydantic import BaseModel


class SearchResult(BaseModel):
    title: str
    source: str
    content: str
    score: float

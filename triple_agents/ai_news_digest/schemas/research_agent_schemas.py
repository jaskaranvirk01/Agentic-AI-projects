from pydantic import BaseModel, HttpUrl
from typing import Optional, Literal


class Article(BaseModel):
    title: str
    content: str
    url: Optional[HttpUrl] = None
    retrieved_by: Literal["news_search", "web_search"]


class ResearchOutput(BaseModel):
    query: str
    articles: list[Article]

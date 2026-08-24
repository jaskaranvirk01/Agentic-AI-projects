from pydantic import BaseModel
from datetime import datetime


class NewsArticle(BaseModel):
    title: str
    summary: str
    source: str
    url: str
    published_at: datetime


class CompanyNews(BaseModel):
    ticker: str
    articles: list[NewsArticle]

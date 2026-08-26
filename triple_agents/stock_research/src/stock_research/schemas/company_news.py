from pydantic import BaseModel
from datetime import datetime


class NewsArticle(BaseModel):
    title: str
    summary: str
    source: str
    url: str
    time_published: datetime


class CompanyNews(BaseModel):
    ticker: str
    articles: list[NewsArticle]

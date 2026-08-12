from schemas.research_agent_schemas import Article
from pydantic import BaseModel
from typing import Literal


class ArticleAnalysis(BaseModel):
    sentiment: Literal[
        "Positive",
        "Neutral",
        "Negative",
    ]

    importance: Literal[
        "High",
        "Medium",
        "Low",
    ]


class AnalyzedArticle(Article):
    sentiment: Literal[
        "Positive",
        "Neutral",
        "Negative",
    ]

    importance: Literal[
        "High",
        "Medium",
        "Low",
    ]


class ArticleAnalysisList(BaseModel):
    analysis: list[ArticleAnalysis]


class AnalysisOutput(BaseModel):
    articles: list[AnalyzedArticle]

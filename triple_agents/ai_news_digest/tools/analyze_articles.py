from langchain_core.tools import tool

from llm.client import llm
from prompts.analysis_prompts import ANALYSIS_PROMPT
from schemas.analysis_agent_schema import (
    AnalyzedArticle, AnalysisOutput, ArticleAnalysisList
)
from schemas.research_agent_schemas import Article
from llm.wrapper import invoke_llm

analysis_llm = llm.with_structured_output(
    ArticleAnalysisList
)


@tool
def analyze_articles(
    articles: list[Article],
) -> AnalysisOutput:
    """Analyze sentiment and importance for each article."""

    if not articles:
        return []

    formatted_articles = "\n\n".join(
        f"""Article {i + 1}

Title:
{article.title}

Content:
{article.content}
"""
        for i, article in enumerate(articles)
    )

    final_prompt = ANALYSIS_PROMPT.format(
        articles=formatted_articles
    )

    analysis = invoke_llm(model=analysis_llm, prompt=final_prompt)
    analyzed_results = analysis.analysis

    analyzed_articles = [
        AnalyzedArticle(
            **article.model_dump(),
            **result.model_dump(),
        )
        for article, result in zip(articles, analyzed_results)
    ]

    return AnalysisOutput(articles=analyzed_articles)

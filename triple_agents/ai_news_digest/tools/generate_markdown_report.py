from langchain_core.tools import tool
from schemas.analysis_agent_schema import AnalyzedArticle
from llm.client import llm
from llm.wrapper import invoke_llm
from prompts.writer_prompts import MARKDOWN_GENEATOR_PROMPT


@tool
def generate_markdown_report(
    articles: list[AnalyzedArticle],
) -> str:
    """Generate a markdown report from analyzed articles."""

    if not articles:
        return "# Daily AI News Digest\n\nNo articles found."

    formatted_articles = "\n\n".join(
        f"""Article {i + 1}

Title:
{article.title}

Importance:
{article.importance}

Sentiment:
{article.sentiment}

Content:
{article.content}

URL:
{article.url}
"""
        for i, article in enumerate(articles)
    )

    final_prompt = MARKDOWN_GENEATOR_PROMPT.format(
        articles=formatted_articles
    )

    response = invoke_llm(model=llm, prompt=final_prompt)

    return response.content

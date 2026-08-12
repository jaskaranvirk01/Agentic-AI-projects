import re
from langchain_core.tools import tool
from rapidfuzz import fuzz

from schemas.research_agent_schemas import Article


def _normalize(title: str) -> str:
    """Normalize a title for fuzzy comparison."""
    title = title.lower()
    title = re.sub(r"[^\w\s]", "", title)
    return " ".join(title.split())


SIMILARITY_THRESHOLD = 90


@tool
def remove_duplicates(articles: list[Article]) -> list[Article]:
    """Remove duplicate articles based on title similarity."""

    unique_articles = []
    normalized_titles = []

    for article in articles:
        normalized = _normalize(article.title)
        is_duplicate = False

        for unique_title in normalized_titles:
            score = fuzz.token_set_ratio(normalized, unique_title)

            if score >= SIMILARITY_THRESHOLD:
                is_duplicate = True
                break

        if not is_duplicate:
            unique_articles.append(article)
            normalized_titles.append(normalized)

    return unique_articles

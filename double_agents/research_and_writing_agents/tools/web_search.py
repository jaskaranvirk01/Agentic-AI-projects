from schemas.search_result import SearchResult
import os
from langchain.tools import tool
from tavily import TavilyClient
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)


@tool
def web_search(user_query: str) -> list[SearchResult]:
    """Search the web for recent and factual information related to the user's query."""
    try:
        results = tavily_client.search(
            query=user_query, search_depth='advanced', max_results=5)

        if not results or not results.get("results"):
            return []

        web_results = []

        for result in results.get("results", []):

            article = SearchResult(
                title=result["title"],
                source=result["url"],
                content=result["content"],
                score=result["score"],
            )

            web_results.append(article)

        return [article.model_dump() for article in web_results]

    except Exception:
        return []

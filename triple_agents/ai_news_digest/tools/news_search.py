import feedparser
from langchain_core.tools import tool
from schemas.research_agent_schemas import Article, ResearchOutput
from dotenv import load_dotenv
from urllib.parse import quote_plus
load_dotenv()


@tool
def news_search(query: str) -> ResearchOutput:
    '''Searches across the web to collect news for given query'''
    try:
        url = (
            f"https://news.google.com/rss/search"
            f"?q={quote_plus(query)}"
            "&hl=en-US&gl=US&ceid=US:en"
        )

        feed = feedparser.parse(url)
    except Exception as e:
        return f'News Search Error: {e}'

    articles = []

    for item in feed.entries:
        articles.append(
            Article(
                title=getattr(item, "title", ""),
                content=getattr(item, "summary", ""),
                url=getattr(item, "link", ""),
                retrieved_by='news_search'
            )
        )

    return ResearchOutput(
        query=query,
        articles=articles
    )

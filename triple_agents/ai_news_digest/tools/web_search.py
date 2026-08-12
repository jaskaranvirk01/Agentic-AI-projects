from tavily import TavilyClient
from dotenv import load_dotenv
import os
from langchain_core.tools import tool
from schemas.research_agent_schemas import Article, ResearchOutput
load_dotenv()


API_KEY = os.getenv('TAVILY_API_KEY')
client = TavilyClient(api_key=API_KEY)


@tool
def web_search(query: str) -> ResearchOutput:
    '''Search the web for the provided query'''
    try:
        response = client.search(query=query, max_results=2)
        print(response)
    except Exception as e:
        print(f'Web Search error: {e} ')

    articles = []

    for result in response.get('results', []):
        articles.append(Article(
            title=result.get('title'),
            content=result.get('content'),
            url=result.get('url'),
            retrieved_by='web_search'
        ))

    return ResearchOutput(
        query=query,
        articles=articles
    )

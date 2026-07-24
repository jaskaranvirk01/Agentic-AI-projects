from dotenv import load_dotenv
from langchain.tools import tool
from tavily import TavilyClient
import os
load_dotenv()

TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')

tavily_client = TavilyClient(api_key=TAVILY_API_KEY)


@tool
def web_search(query: str) -> str:
    '''Search a query on web'''
    try:
        response = tavily_client.search(
            query=query, max_results=5, search_depth='basic')

        results = response.get('results', [])

        if not results:
            return f'No search results for query :{query}'

        answer = []
        for result in results:
            answer.append(
                f"""
                Title   : {result.get("title")}

                Summary : {result.get("content")}

                Source  : {result.get("url")}
                """
            )

        return '\n'.join(answer)

    except Exception as e:
        return f'Unable to search on web \nError : {e}'

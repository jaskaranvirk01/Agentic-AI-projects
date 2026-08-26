from stock_research.utils.news_normalizer import normalize_company_news
from stock_research.clients.alpha_vantage import alpha_vantage_client
from langchain_core.tools import tool
from stock_research.schemas.company_news import CompanyNews


@tool
def get_company_news(ticker: str) -> CompanyNews:
    '''This tool uses an api to search relevant news articles for the required company via its ticker and returns formatted response'''
    news_data = alpha_vantage_client.get_company_news(ticker)
    return normalize_company_news(ticker, news_data)

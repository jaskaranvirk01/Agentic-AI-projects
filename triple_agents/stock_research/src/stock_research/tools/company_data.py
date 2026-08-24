from stock_research.clients.alpha_vantage import alpha_vantage_client
from stock_research.utils.market_data_normalizer import normalize_market_data
from langchain_core.tools import tool
from stock_research.schemas.market import CompanyMarketData


@tool
def get_company_data(ticker: str) -> CompanyMarketData:
    '''This tool retrieves basic company information and current market quotefor a stock ticker. 
    Use it when you need company profile or current
    market data for a publicly traded company.'''
    company_data = alpha_vantage_client.get_company_overview(ticker)
    global_quote = alpha_vantage_client.get_global_quote(ticker)

    return normalize_market_data(company_data, global_quote)

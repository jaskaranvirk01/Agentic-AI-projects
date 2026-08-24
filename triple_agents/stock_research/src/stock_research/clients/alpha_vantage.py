from stock_research.config.settings import settings
from httpx import Client


class AlphaVantageClient:

    def __init__(self, client: Client, base_url: str, api_key: str):
        self.client = client
        self.base_url = base_url
        self.api_key = api_key

    def get_company_overview(self, ticker: str) -> dict:
        """Uses the financial API to search for the given firm information."""

        response = self.client.get(
            self.base_url,
            params={
                "function": "OVERVIEW",
                "symbol": ticker,
                "apikey": self.api_key,
            },
        )

        response.raise_for_status()
        return response.json()

    def get_global_quote(self, ticker: str) -> dict:
        """Uses the financial API to get global quote for the given firm."""

        response = self.client.get(
            self.base_url,
            params={
                "function": "GLOBAL_QUOTE",
                "symbol": ticker,
                "apikey": self.api_key,
            },
        )

        response.raise_for_status()
        return response.json()

    def get_company_news(self, ticker: str) -> dict:
        '''Uses an external api to get news about the specific company'''
        response = self.client.get(
            self.base_url,
            params={
                'function': 'NEWS_SENTIMENT',
                'tickers': ticker,
                'apikey': self.api_key
            }
        )

        response.raise_for_status()
        return response.json()

    def close(self):
        """Closes the client."""
        self.client.close()


httpx_client = Client(timeout=30.0)

alpha_vantage_client = AlphaVantageClient(
    client=httpx_client,
    base_url=settings.alpha_vantage_base_url,
    api_key=settings.alpha_vantage_api_key,
)

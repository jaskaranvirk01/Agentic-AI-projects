from pydantic import BaseModel


class CompanyMarketData(BaseModel):
    ticker: str
    company_name: str
    sector: str
    industry: str
    description: str
    market_cap: int
    current_price: float
    price_change: float
    price_change_percent: float
    volume: int

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
    pe_ratio: float
    forward_pe: float
    peg_ratio: float
    price_to_sales: float
    price_to_book: float
    ev_to_revenue: float
    ev_to_ebitda: float
    eps: float
    profit_margin: float
    operating_margin: float
    return_on_assets: float
    return_on_equity: float
    revenue_ttm: int
    quarterly_revenue_growth: float
    quarterly_earnings_growth: float
    dividend_per_share: float
    dividend_yield: float
    beta: float
    fifty_two_week_high: float
    fifty_two_week_low: float

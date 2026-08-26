from pydantic import BaseModel
from stock_research.schemas.company_news import CompanyNews
from stock_research.schemas.market import CompanyMarketData


class MarketResearchData(BaseModel):
    company_market_data: CompanyMarketData
    company_news: CompanyNews


class LlmInput(BaseModel):
    market_research_data: MarketResearchData


class LlmOutput(BaseModel):
    market_overview: str
    notable_recent_developments: str
    positive_factors: str
    key_concerns: str


class ResearchAgentOutput(BaseModel):
    research_data: MarketResearchData
    analysis: LlmOutput

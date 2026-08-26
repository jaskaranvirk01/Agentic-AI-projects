from typing import TypedDict
from stock_research.schemas.research import ResearchAgentOutput
from stock_research.schemas.financial import FinancialAnalysisOutput


class StockResearchState(TypedDict):
    ticker: str
    research: ResearchAgentOutput | None
    financial_analysis: FinancialAnalysisOutput | None
    final_report: None

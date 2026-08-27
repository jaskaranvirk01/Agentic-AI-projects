from typing import TypedDict
from stock_research.schemas.research import ResearchAgentOutput
from stock_research.schemas.financial import FinancialAnalysisOutput
from stock_research.schemas.final_report import FinalReport


class StockResearchState(TypedDict):
    ticker: str
    research: ResearchAgentOutput | None
    financial_analysis: FinancialAnalysisOutput | None
    final_report: FinalReport | None

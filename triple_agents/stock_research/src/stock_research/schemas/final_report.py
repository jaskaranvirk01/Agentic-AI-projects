from pydantic import BaseModel
from stock_research.schemas.research import ResearchAgentOutput
from stock_research.schemas.financial import FinancialAnalysisOutput


class FinalReport(BaseModel):
    executive_summary: str
    business_overview: str
    market_position: str
    financial_performance: str
    valuation: str
    recent_developments: str
    key_strengths: str
    key_risks: str
    investment_outlook: str
    overall_assessment: str


class ReportGenerationInput(BaseModel):
    research_data: ResearchAgentOutput
    financial_analysis: FinancialAnalysisOutput

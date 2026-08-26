from pydantic import BaseModel


class FinancialAnalysisOutput(BaseModel):
    valuation_analysis: str
    profitability_analysis: str
    growth_analysis: str
    financial_strength: str
    risk_analysis: str
    overall_assessment: str

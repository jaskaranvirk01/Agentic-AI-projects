from stock_research.schemas.research import ResearchAgentOutput
from stock_research.schemas.financial import FinancialAnalysisOutput
from stock_research.schemas.final_report import ReportGenerationInput
from stock_research.schemas.final_report import FinalReport
from stock_research.llm.client import llm
from langchain_core.messages import SystemMessage, HumanMessage


class FinalReportWriterAgent:
    def __init__(self):
        self.llm = llm
        self.llm_with_structured_output = self.llm.with_structured_output(
            FinalReport)
        self.writing_system_prompt = SystemMessage(content='')

    def run(self, research_data: ResearchAgentOutput, financial_analysis: FinancialAnalysisOutput) -> FinalReport:
        data = ReportGenerationInput(
            research_data=research_data, financial_analysis=financial_analysis)
        messages = [self.writing_system_prompt, HumanMessage(
            content=data.model_dump_json(indent=2))]

        return self.llm_with_structured_output.invoke(messages)

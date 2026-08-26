from stock_research.llm.client import llm
from stock_research.schemas.financial import FinancialAnalysisOutput
from stock_research.schemas.market import CompanyMarketData
from langchain_core.messages import SystemMessage, HumanMessage
from stock_research.prompts.financial_analysis_prompt import SYSTEM_PROMPT


class FinancialAnalysisAgent:
    def __init__(self):
        self.llm = llm
        self.llm_with_structured_output = self.llm.with_structured_output(
            FinancialAnalysisOutput)
        self.system_prompt = SystemMessage(content=SYSTEM_PROMPT)

    def run(self, data: CompanyMarketData) -> FinancialAnalysisOutput:
        messages = [self.system_prompt, HumanMessage(
            content=data.model_dump_json())]

        return self.llm_with_structured_output.invoke(messages)


financial_analysis_agent = FinancialAnalysisAgent()

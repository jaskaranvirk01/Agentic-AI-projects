from stock_research.tools.company_news import get_company_news
from stock_research.tools.company_data import get_company_data
from stock_research.llm.client import llm
from stock_research.schemas.research import LlmOutput, LlmInput, MarketResearchData, ResearchAgentOutput
from langchain.messages import SystemMessage, HumanMessage
import time
from stock_research.prompts.market_research_prompts import SYSTEM_PROMPT


class MarketResearchAgent:
    def __init__(self):
        self.llm = llm
        self.get_company_data = get_company_data
        self.get_company_news = get_company_news
        self.llm_with_structured_output = self.llm.with_structured_output(
            LlmOutput)
        self.llm_analysis_prompt = SystemMessage(content=SYSTEM_PROMPT)

    def run(self, ticker: str) -> ResearchAgentOutput:

        company_market_data = self.get_company_data.invoke(ticker)
        time.sleep(1)
        company_news = self.get_company_news.invoke(ticker)

        market_research_data = MarketResearchData(
            company_market_data=company_market_data, company_news=company_news)

        llm_input = LlmInput(market_research_data=market_research_data)

        messages = [
            self.llm_analysis_prompt,
            HumanMessage(content=llm_input.model_dump_json()),
        ]
        llm_analysis = self.llm_with_structured_output.invoke(messages)

        return ResearchAgentOutput(
            research_data=market_research_data,
            analysis=llm_analysis
        )


market_research_agent = MarketResearchAgent()

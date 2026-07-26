from agents.base_agent import BaseAgent
from prompts.research_agent_prompt import SYSTEM_PROMPT
from tools.web_search import web_search
from tools.calculator import calculator
from llm.client import llm
from langchain_core.messages import HumanMessage
tools = [web_search, calculator]


class ResearchAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            llm=llm,
            tools=[web_search, calculator],
            system_prompt=SYSTEM_PROMPT
        )

    def invoke(self, user_query: str):
        self.messages.append(HumanMessage(content=user_query))
        response = self.llm_with_tools.invoke(self.messages)
        self.messages.append(response)
        return response


research_agent = ResearchAgent()

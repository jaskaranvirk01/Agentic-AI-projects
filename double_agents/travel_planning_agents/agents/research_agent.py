from langchain_core.messages import HumanMessage
from llm.client import llm
from agents.base_agent import BaseAgent
from tools.search_flights import search_flights
from tools.get_weather import get_weather
from prompts.research_agent import RESEARCH_AGENT_SYSTEM_PROMPT
tools = [get_weather, search_flights]


class ResearchAgent(BaseAgent):
    def __init__(self, ):
        super().__init__(llm=llm, tools=tools, system_prompt=RESEARCH_AGENT_SYSTEM_PROMPT)

    def invoke(self, user_query: str):
        self.messages.append(HumanMessage(content=user_query))
        return self.continue_conversation()


research_agent = ResearchAgent()

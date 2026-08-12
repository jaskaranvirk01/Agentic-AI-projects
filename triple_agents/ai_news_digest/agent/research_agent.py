from agent.base_agent import BaseAgent
from llm.client import llm
from prompts.researcher_prompts import SYSTEM_PROMPT
from langchain_core.messages import HumanMessage
from tools.web_search import web_search
from tools.news_search import news_search


class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            llm=llm,
            tools=[web_search, news_search],
            system_prompt=SYSTEM_PROMPT)

    def invoke(self, user_query: str):
        self.messages.append(HumanMessage(content=user_query))
        return self.continue_conversation()


research_agent = ResearchAgent()

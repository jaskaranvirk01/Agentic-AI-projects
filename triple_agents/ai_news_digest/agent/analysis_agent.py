from agent.base_agent import BaseAgent
from llm.client import llm
from prompts.analysis_prompts import SYSTEM_PROMPT
from tools.analyze_articles import analyze_articles
from tools.remove_duplicates import remove_duplicates
from schemas.research_agent_schemas import ResearchOutput
from langchain_core.messages import HumanMessage


class AnalysisAgent(BaseAgent):
    def __init__(self,):
        super().__init__(llm=llm,
                         tools=[remove_duplicates, analyze_articles],
                         system_prompt=SYSTEM_PROMPT)

    def invoke(self, research_output: ResearchOutput):
        self.messages.append(HumanMessage(
            content=research_output.model_dump_json(indent=2)
        ))
        return self.continue_conversation()


analysis_agent = AnalysisAgent()

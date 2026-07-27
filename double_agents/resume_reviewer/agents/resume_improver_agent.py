from agents.base_agent import BaseAgent
from llm.client import llm
from tools.ats_scorer import ats_scorer
from tools.rewrite_resume import rewrite_resume
from prompts.resume_improver_agent import RESUME_IMPROVER_SYSTEM_PROMPT
from schema.resume_analyzer import ResumeAnalysisResponse
from langchain_core.messages import HumanMessage
tools = [ats_scorer, rewrite_resume]


class ResumeImproveAgent(BaseAgent):
    def __init__(self,):
        super().__init__(llm=llm, tools=tools, system_prompt=RESUME_IMPROVER_SYSTEM_PROMPT)

    def invoke(self, data: ResumeAnalysisResponse):
        self.messages.append(
            HumanMessage(
                content=data.model_dump_json(indent=2)
            )
        )
        return self.continue_conversation()


resume_improve_agent = ResumeImproveAgent()

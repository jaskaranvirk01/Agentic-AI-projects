from agent.base_agent import BaseAgent
from llm.client import llm
from langchain_core.messages import HumanMessage
from schemas.analysis_agent_schema import AnalysisOutput
from tools.generate_markdown_report import generate_markdown_report
from tools.grammar_check import grammar_check
from prompts.writer_prompts import SYSTEM_PROMPT


class WriterAgent(BaseAgent):
    def __init__(self):
        super().__init__(llm=llm,
                         tools=[generate_markdown_report, grammar_check],
                         system_prompt=SYSTEM_PROMPT)

    def invoke(self, analysis_output: AnalysisOutput):
        self.messages.append(HumanMessage(
            content=analysis_output.model_dump_json(indent=2)
        ))
        return self.continue_conversation()


writer_agent = WriterAgent()

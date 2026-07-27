from llm.client import llm
from agents.base_agent import BaseAgent
from tools.info_extractor import extract_resume_information
from tools.resume_reader import read_pdf
from langchain_core.messages import HumanMessage
from prompts.resume_reader_agent import RESUME_READER_SYSTEM_PROMPT
tools = [extract_resume_information, read_pdf]


class ResumeReaderAgent(BaseAgent):
    def __init__(self):
        super().__init__(llm=llm, tools=tools, system_prompt=RESUME_READER_SYSTEM_PROMPT)

    def invoke(self, user_query: str):
        self.messages.append(HumanMessage(content=user_query))
        return self.continue_conversation()


resume_reader_agent = ResumeReaderAgent()

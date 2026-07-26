from llm.client import llm
from agents.base_agent import BaseAgent
from prompts.writer_agent_prompt import SYSTEM_PROMPT
from tools.check_grammar import check_grammar
from tools.markdown_formatter import markdown_formatter
from langchain_core.messages import HumanMessage
from schemas.research_output import ResearchOutput
tools = [check_grammar, markdown_formatter]


class WriterAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            llm=llm,
            tools=[check_grammar, markdown_formatter],
            system_prompt=SYSTEM_PROMPT
        )

    def invoke(self, context: ResearchOutput):
        self.messages.append(
            HumanMessage(
                content=str(context.model_dump())
            )
        )
        response = self.llm_with_tools.invoke(self.messages)
        self.messages.append(response)
        return response


writer_agent = WriterAgent()

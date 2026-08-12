from langchain_core.tools import tool
from prompts.writer_prompts import GRAMMER_CHECKER_PROMPT
from llm.client import llm
from llm.wrapper import invoke_llm
grammar_llm = llm


@tool
def grammar_check(report: str) -> str:
    '''
    Improve the grammar and  readability of a markdown report
    '''

    if not report.strip():
        return report

    final_prompt = GRAMMER_CHECKER_PROMPT.format(report=report)

    response = invoke_llm(model=grammar_llm, prompt=final_prompt)
    return response.content

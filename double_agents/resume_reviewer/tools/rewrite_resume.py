from langchain_core.tools import tool

from llm.client import llm
from prompts.resume_rewriter import RESUME_REWRITER_PROMPT
from schema.resume_improver import (
    ResumeRewriteInput,
    ResumeRewriteResponse,
)


@tool
def rewrite_resume(
    input_resume_data: ResumeRewriteInput,
) -> ResumeRewriteResponse:
    """
    Rewrite and optimize the resume using the resume analysis and ATS evaluation.
    """

    structured_llm = llm.with_structured_output(
        ResumeRewriteResponse
    )

    prompt = RESUME_REWRITER_PROMPT.format(
        resume_analysis=input_resume_data.resume_analysis.model_dump_json(
            indent=2),
        ats_score=input_resume_data.ats_score.model_dump_json(indent=2),
    )

    return structured_llm.invoke(prompt)

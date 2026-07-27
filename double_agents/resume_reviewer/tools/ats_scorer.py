from langchain_core.tools import tool

from llm.client import llm
from prompts.ats_scorer import ATS_SCORER_PROMPT
from schema.resume_analyzer import ResumeAnalysisResponse
from schema.resume_improver import ATSScoreResponse


@tool
def ats_scorer(
    resume_analysis: ResumeAnalysisResponse,
) -> ATSScoreResponse:
    """
    Evaluate the ATS compatibility of the provided resume analysis.
    """

    structured_llm = llm.with_structured_output(
        ATSScoreResponse
    )

    prompt = ATS_SCORER_PROMPT.format(
        resume_analysis=resume_analysis.model_dump_json(indent=2)
    )

    return structured_llm.invoke(prompt)

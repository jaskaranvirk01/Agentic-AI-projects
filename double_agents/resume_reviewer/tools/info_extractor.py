from langchain.tools import tool

from llm.client import llm
from prompts.info_extractor import RESUME_INFORMATION_EXTRACTOR_PROMPT
from schema.resume_analyzer import (
    ReadPdfResponse,
    ResumeAnalysisResponse,
)


@tool
def extract_resume_information(resume: ReadPdfResponse,) -> ResumeAnalysisResponse:
    """Extract all relevant resume information into a structured format."""

    structured_llm = llm.with_structured_output(
        ResumeAnalysisResponse
    )

    prompt = RESUME_INFORMATION_EXTRACTOR_PROMPT.format(
        resume=resume.raw_text
    )

    return structured_llm.invoke(prompt)

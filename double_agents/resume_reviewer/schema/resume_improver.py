from pydantic import BaseModel
from schema.resume_analyzer import ResumeAnalysisResponse


class ATSScoreResponse(BaseModel):
    overall_score: int
    keyword_score: int
    formatting_score: int
    content_score: int
    suggestions: list[str]


class ResumeRewriteInput(BaseModel):
    resume_analysis: ResumeAnalysisResponse
    ats_score: ATSScoreResponse


class ResumeRewriteResponse(BaseModel):
    improved_resume: str

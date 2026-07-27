from pydantic import BaseModel


class ReadPdfResponse(BaseModel):
    raw_text: str


class ResumeAnalysisResponse(BaseModel):
    name: str
    email: str
    phone: str

    summary: str

    skills: list[str]

    education: list[str]

    experience: list[str]

    projects: list[str]

    certifications: list[str]

    strengths: list[str]

    weaknesses: list[str]

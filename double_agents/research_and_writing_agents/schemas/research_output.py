from pydantic import BaseModel


class ResearchOutput(BaseModel):
    user_query: str
    research: str

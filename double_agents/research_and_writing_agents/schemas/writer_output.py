from pydantic import BaseModel


class WriterOutput(BaseModel):
    markdown: str

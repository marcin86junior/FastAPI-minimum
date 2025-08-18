from pydantic import BaseModel, Field


class Task(BaseModel):
    title: str = Field(..., max_length=255, description="Tytuł zadania")
    description: str | None = Field(None, max_length=1024, description="Opcjonalny opis zadania")

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str = Field(..., max_length=255, description="Tytuł zadania")
    description: str | None = Field(None, max_length=1024, description="Opcjonalny opis zadania")


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
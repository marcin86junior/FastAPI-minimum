from pydantic import BaseModel


class KotBase(BaseModel):
    imie: str
    rasa: str | None = None


class KotCreate(KotBase):
    pass


class KotSchema(KotBase):
    id: int

    class Config:
        from_attributes = True
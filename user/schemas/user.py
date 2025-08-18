from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(BaseModel):
    username: str  # Pole wymagane
    email: EmailStr
    password: str


class UserSchema(UserBase):
    id: int

    class Config:
        from_attributes = True

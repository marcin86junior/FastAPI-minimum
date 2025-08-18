from pydantic import BaseModel
from typing import List, Optional


class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    pass


class TagSchema(TagBase):
    id: int

    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    name: str
    sku: str
    price: float
    description: Optional[str] = None


class ProductCreate(ProductBase):
    tags: List[TagCreate] = []


class ProductSchema(ProductBase):
    id: int
    tags: List[TagSchema] = []

    class Config:
        from_attributes = True
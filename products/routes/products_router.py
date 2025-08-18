from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from core.database import get_db
from products.schemas.products import ProductCreate, ProductSchema
from products.services.products_service import get_products, get_product, create_product, delete_product
from products.models.products import Product, Tag
from sqlalchemy.sql import and_
from sqlalchemy import func  # Dodaj import func

product_router = APIRouter(
    prefix='/products',
    tags=['Products']
)


@product_router.get('/', response_model=list[ProductSchema])
def list_products(
    name: str = Query(None, description="Search by product name"),
    price: float = Query(None, description="Search by product price"),
    tags: list[str] = Query(None, description="Search by one or more tags"),
    db: Session = Depends(get_db)
):
    query = db.query(Product)

    if name:
        query = query.filter(Product.name.ilike(f"%{name}%"))
    if price:
        query = query.filter(Product.price == price)
    if tags:
        query = (
            query.join(Product.tags)
            .filter(Tag.name.in_(tags))
            .group_by(Product.id)
            .having(func.count(Tag.id) == len(tags))  # Użyj func.count zamiast db.func.count
        )

    return query.all()


@product_router.get('/{product_id}', response_model=ProductSchema)
def retrieve_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@product_router.post('/', response_model=ProductSchema)
def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)


@product_router.delete('/{product_id}')
def remove_product(product_id: int, db: Session = Depends(get_db)):
    delete_product(db, product_id)
    return {"detail": "Product deleted"}

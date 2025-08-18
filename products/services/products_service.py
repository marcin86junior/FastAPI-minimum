from sqlalchemy.orm import Session
from products.models.products import Product, Tag
from products.schemas.products import ProductCreate


def get_products(db: Session):
    return db.query(Product).all()


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def create_product(db: Session, product: ProductCreate):
    db_product = Product(
        name=product.name,
        sku=product.sku,
        price=product.price,
        description=product.description
    )
    for tag_data in product.tags:
        tag = db.query(Tag).filter(Tag.name == tag_data.name).first()
        if not tag:
            tag = Tag(name=tag_data.name)
        db_product.tags.append(tag)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
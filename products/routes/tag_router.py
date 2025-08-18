from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from products.models.products import Tag
from products.schemas.products import TagCreate, TagSchema

tag_router = APIRouter(
    prefix='/tags',
    tags=['Tags']
)


@tag_router.get('/', response_model=list[TagSchema])
def list_tags(db: Session = Depends(get_db)):
    return db.query(Tag).all()


@tag_router.get('/{tag_id}', response_model=TagSchema)
def retrieve_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag


@tag_router.post('/', response_model=TagSchema)
def create_tag(tag: TagCreate, db: Session = Depends(get_db)):
    db_tag = db.query(Tag).filter(Tag.name == tag.name).first()
    if db_tag:
        raise HTTPException(status_code=400, detail="Tag already exists")
    new_tag = Tag(name=tag.name)
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return new_tag


@tag_router.delete('/{tag_id}')
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    db.delete(tag)
    db.commit()
    return {"detail": "Tag deleted"}

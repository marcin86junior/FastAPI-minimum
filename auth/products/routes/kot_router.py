from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from kot.schemas.kot import KotCreate, KotSchema
from kot.services.kot_service import get_koty, get_kot, create_kot, delete_kot


kot_router = APIRouter(
    prefix='/kot',
    tags=['Koty']
)


@kot_router.get('/koty', response_model=list[KotSchema])
def list_koty(db: Session = Depends(get_db)):
    return get_koty(db)


@kot_router.get('/koty/{kot_id}', response_model=KotSchema)
def retrieve_kot(kot_id: int, db: Session = Depends(get_db)):
    kot = get_kot(db, kot_id)
    if not kot:
        raise HTTPException(status_code=404, detail="Kot nie znaleziony")
    return kot


@kot_router.post('/koty', response_model=KotSchema)
def create_new_kot(kot: KotCreate, db: Session = Depends(get_db)):
    return create_kot(db, kot)


@kot_router.delete('/koty/{kot_id}')
def remove_kot(kot_id: int, db: Session = Depends(get_db)):
    delete_kot(db, kot_id)
    return {"detail": "Kot usunięty"}
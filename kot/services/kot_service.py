from sqlalchemy.orm import Session
from kot.models.kot import Kot
from kot.schemas.kot import KotCreate


def get_koty(db: Session):
    return db.query(Kot).all()


def get_kot(db: Session, kot_id: int):
    return db.query(Kot).filter(Kot.id == kot_id).first()


def create_kot(db: Session, kot: KotCreate):
    db_kot = Kot(imie=kot.imie, rasa=kot.rasa)
    db.add(db_kot)
    db.commit()
    db.refresh(db_kot)
    return db_kot


def delete_kot(db: Session, kot_id: int):
    db_kot = db.query(Kot).filter(Kot.id == kot_id).first()
    if db_kot:
        db.delete(db_kot)
        db.commit()
    return
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from core.database import Base


class Kot(Base):
    __tablename__ = 'koty'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    imie: Mapped[str] = mapped_column(String(32), nullable=False)
    rasa: Mapped[str] = mapped_column(String(64), nullable=True)
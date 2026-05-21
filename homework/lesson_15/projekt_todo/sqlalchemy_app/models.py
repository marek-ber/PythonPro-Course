import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


zadanie_tag = Table(
    "zadanie_tag",
    Base.metadata,
    Column("zadanie_id", Integer, ForeignKey("zadania.id")),
    Column("tag_id", Integer, ForeignKey("tagi.id")),
)


class Zadanie(Base):
    __tablename__ = "zadania"

    id = Column(Integer, primary_key=True)
    opis = Column(String, nullable=False)
    zrobione = Column(Boolean, default=False, nullable=False)
    data_utworzenia = Column(DateTime, default=datetime.datetime.utcnow)

    tagi = relationship(
        "Tag",
        secondary=zadanie_tag,
        back_populates="zadania"
    )

    def __repr__(self):
        return f"<Zadanie(id={self.id}, opis='{self.opis}')>"


class Tag(Base):
    __tablename__ = "tagi"

    id = Column(Integer, primary_key=True)
    nazwa = Column(String, nullable=False, unique=True)

    zadania = relationship(
        "Zadanie",
        secondary=zadanie_tag,
        back_populates="tagi"
    )

    def __repr__(self):
        return f"<Tag(id={self.id}, nazwa='{self.nazwa}')>"
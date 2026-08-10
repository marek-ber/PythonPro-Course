# 7. ✏ (Proste) SQLAlchemy Async - Definicja Modelu: Zdefiniuj model Product używając
# DeclarativeBase z SQLAlchemy . Model powinien mieć pola: id (int, klucz główny),
# name (String(100)) oraz price (Integer, przechowujący cenę w groszach).


from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(Integer)

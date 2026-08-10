# 20. 🧠 (Challenge) SQLAlchemy Async - JOIN: (Znacie JOIN). Dodaj do modelu Product
# relację ForeignKey do User (twórca produktu). Zmodyfikuj handler GET
# /products/{id} , aby pobierał produkt wraz z nazwą użytkownika, który go stworzył
# (używając select(Product, User).join(User) lub
# options(joinedload(Product.user)) - opcja dla ambitnych).


from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, String


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)

    products: Mapped[list["Product"]] = relationship(back_populates="user")

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
        }


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(Integer)
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True)

    user: Mapped[User | None] = relationship(back_populates="products")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "user_id": self.user_id,
        }


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    balance: Mapped[int] = mapped_column(Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "balance": self.balance,
        }

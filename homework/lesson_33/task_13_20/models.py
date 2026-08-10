from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class AuthorORM(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(120), unique=True)

    books: Mapped[list["BookORM"]] = relationship(
        back_populates="author",
        cascade="all, delete-orphan",
    )


class BookORM(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    price: Mapped[float] = mapped_column(Float)
    category: Mapped[str] = mapped_column(String(50))
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))

    author: Mapped[AuthorORM] = relationship(back_populates="books")


class UserORM(Base):
    __tablename__ = "blog_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String(120), unique=True)

    posts: Mapped[list["PostORM"]] = relationship(
        back_populates="author",
        cascade="all, delete-orphan",
    )
    comments: Mapped[list["CommentORM"]] = relationship(
        back_populates="author",
        cascade="all, delete-orphan",
    )


class PostORM(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(ForeignKey("blog_users.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    author: Mapped[UserORM] = relationship(back_populates="posts")
    comments: Mapped[list["CommentORM"]] = relationship(
        back_populates="post",
        cascade="all, delete-orphan",
    )


class CommentORM(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String(500))
    author_id: Mapped[int] = mapped_column(ForeignKey("blog_users.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    author: Mapped[UserORM] = relationship(back_populates="comments")
    post: Mapped[PostORM] = relationship(back_populates="comments")

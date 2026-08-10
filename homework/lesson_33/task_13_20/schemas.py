from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class AuthorCreate(BaseModel):
    name: str
    email: EmailStr


class AuthorResponse(AuthorCreate):
    id: int

    model_config = {"from_attributes": True}


class BookCreate(BaseModel):
    title: str = Field(..., min_length=2)
    price: float = Field(..., gt=0)
    category: str
    author_id: int


class BookUpdate(BaseModel):
    title: str | None = None
    price: float | None = Field(None, gt=0)
    category: str | None = None
    author_id: int | None = None


class BookResponse(BookCreate):
    id: int

    model_config = {"from_attributes": True}


class AuthorWithBooks(AuthorResponse):
    books: list[BookResponse] = []


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr


class UserUpdate(BaseModel):
    username: str | None = Field(None, min_length=3)
    email: EmailStr | None = None


class UserResponse(UserCreate):
    id: int

    model_config = {"from_attributes": True}


class PostCreate(BaseModel):
    title: str = Field(..., min_length=5)
    content: str = Field(..., min_length=10)
    author_id: int


class PostUpdate(BaseModel):
    title: str | None = Field(None, min_length=5)
    content: str | None = Field(None, min_length=10)


class PostResponse(PostCreate):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}


class CommentCreate(BaseModel):
    content: str = Field(..., min_length=1, max_length=500)
    author_id: int


class CommentResponse(CommentCreate):
    id: int
    post_id: int
    created_at: datetime

    model_config = {"from_attributes": True}


class PostWithComments(PostResponse):
    comments: list[CommentResponse] = []

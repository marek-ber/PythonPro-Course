from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr

from dependencies import verify_api_key


router = APIRouter(prefix="/books", tags=["Books"])

BOOKS = {}


class Author(BaseModel):
    name: str
    email: EmailStr


class Book(BaseModel):
    title: str
    author: Author
    price: float


@router.get("/")
async def get_books(api_key: str = Depends(verify_api_key)):
    return list(BOOKS.values())


@router.get("/{book_id}")
async def get_book(book_id: int, api_key: str = Depends(verify_api_key)):
    book = BOOKS.get(book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@router.post("/", status_code=201)
async def create_book(book: Book, api_key: str = Depends(verify_api_key)):
    book_id = max(BOOKS.keys()) + 1 if BOOKS else 1

    new_book = book.model_dump()
    new_book["id"] = book_id
    BOOKS[book_id] = new_book

    return new_book

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Query, status
from sqlalchemy import asc, desc, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from background import send_book_email, update_book_statistics
from database import get_db
from models import AuthorORM, BookORM
from schemas import (
    AuthorCreate,
    AuthorResponse,
    AuthorWithBooks,
    BookCreate,
    BookResponse,
    BookUpdate,
)


router = APIRouter(tags=["Books"])


@router.post("/authors", response_model=AuthorResponse, status_code=201)
async def create_author(author: AuthorCreate, db: AsyncSession = Depends(get_db)):
    new_author = AuthorORM(**author.model_dump())
    db.add(new_author)
    await db.commit()
    await db.refresh(new_author)
    return new_author


@router.get("/authors/{author_id}/books", response_model=AuthorWithBooks)
async def get_author_books(author_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(AuthorORM)
        .options(selectinload(AuthorORM.books))
        .where(AuthorORM.id == author_id)
    )
    author = result.scalar_one_or_none()

    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    return author


@router.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def create_book(
    book: BookCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
):
    author = await db.get(AuthorORM, book.author_id)

    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    new_book = BookORM(**book.model_dump())
    db.add(new_book)
    await db.commit()
    await db.refresh(new_book)

    background_tasks.add_task(send_book_email, new_book.title)
    return new_book


@router.get("/books", response_model=list[BookResponse])
async def get_books(
    skip: int = 0,
    limit: int = Query(10, ge=1, le=100),
    category: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    sort_by: str = "title",
    db: AsyncSession = Depends(get_db),
):
    query = select(BookORM)

    if category:
        query = query.where(BookORM.category == category)
    if min_price is not None:
        query = query.where(BookORM.price >= min_price)
    if max_price is not None:
        query = query.where(BookORM.price <= max_price)

    if sort_by == "price":
        query = query.order_by(asc(BookORM.price))
    elif sort_by == "title":
        query = query.order_by(asc(BookORM.title))
    else:
        raise HTTPException(status_code=400, detail="sort_by must be price or title")

    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()


@router.get("/books/{book_id}", response_model=BookResponse)
async def get_book(book_id: int, db: AsyncSession = Depends(get_db)):
    book = await db.get(BookORM, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@router.put("/books/{book_id}", response_model=BookResponse)
async def update_book(
    book_id: int,
    data: BookUpdate,
    db: AsyncSession = Depends(get_db),
):
    book = await db.get(BookORM, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(book, field, value)

    await db.commit()
    await db.refresh(book)
    return book


@router.delete("/books/{book_id}", status_code=204)
async def delete_book(
    book_id: int,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
):
    book = await db.get(BookORM, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    await db.delete(book)
    await db.commit()

    background_tasks.add_task(update_book_statistics)
    return None

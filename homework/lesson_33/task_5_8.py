# 5.
# ✏️ Zadanie 5 – CRUD w pamięci
# Stwórz proste CRUD API dla książek (dict w pamięci):
# GET /books - lista wszystkich
# GET /books/{id} - jedna książka
# POST /books - dodaj książkę
# DELETE /books/{id} - usuń książkę
# (proste)6.
# ✏️ Zadanie 6 – Status Codes
# Dla zadania 5 dodaj odpowiednie status codes:
# 201 dla POST
# 204 dla DELETE
# 404 gdy książka nie istnieje
# (proste)
# 7.
# ✏️ Zadanie 7 – Walidacja Email
# Utwórz model User z polem email (EmailStr).
# Endpoint POST /users waliduje poprawność emaila.
# (proste)
# 8.
# ✏️ Zadanie 8 – Dokumentacja
# Dla dowolnego API dodaj:
# Tytuł i opis aplikacji
# Tagi do endpoints
# Docstringi z przykładami
# Sprawdź /docs.
# (proste)



from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr


app = FastAPI(
    title="Books API",
    description="Proste API do obsługi książek i użytkowników",
    version="1.0.0",
)

BOOKS = {}


class BookCreate(BaseModel):
    name: str
    year: int
    author: str


class BookResponse(BookCreate):
    id: int


class User(BaseModel):
    name: str
    email: EmailStr


@app.get("/books", tags=["Books"])
async def get_books():
    """Zwraca listę wszystkich książek."""
    return list(BOOKS.values())


@app.get("/books/{book_id}", response_model=BookResponse, tags=["Books"])
async def get_book(book_id: int):
    """Zwraca jedną książkę na podstawie ID."""
    book = BOOKS.get(book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@app.post(
    "/books",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Books"],
)
async def add_book(book: BookCreate):
    """Dodaje nową książkę do pamięci aplikacji."""
    if not BOOKS:
        book_id = 1
    else:
        book_id = max(BOOKS.keys()) + 1

    new_book = book.model_dump()
    new_book["id"] = book_id
    BOOKS[book_id] = new_book

    return new_book


@app.delete(
    "/books/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Books"],
)
async def delete_book(book_id: int):
    """Usuwa książkę. Zwraca 404, jeśli książka nie istnieje."""
    if book_id not in BOOKS:
        raise HTTPException(status_code=404, detail="Book not found")

    del BOOKS[book_id]
    return None


@app.post("/users", tags=["Users"])
async def create_user(user: User):
    """Sprawdza poprawność adresu e-mail dzięki EmailStr."""
    return user

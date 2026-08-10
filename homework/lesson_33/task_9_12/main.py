from fastapi import FastAPI

from routers import authors, books, products


app = FastAPI(
    title="Books API - zadania 9-12",
    description="APIRouter, Dependency Injection, modele zagnieżdżone i walidatory",
)

app.include_router(books.router)
app.include_router(authors.router)
app.include_router(products.router)


@app.get("/")
async def root():
    return {"message": "Books API"}

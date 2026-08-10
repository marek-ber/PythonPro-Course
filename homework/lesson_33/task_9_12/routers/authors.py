from fastapi import APIRouter
from pydantic import BaseModel, EmailStr


router = APIRouter(prefix="/authors", tags=["Authors"])

AUTHORS = {}


class Author(BaseModel):
    name: str
    email: EmailStr


@router.get("/")
async def get_authors():
    return list(AUTHORS.values())


@router.post("/", status_code=201)
async def create_author(author: Author):
    author_id = max(AUTHORS.keys()) + 1 if AUTHORS else 1

    new_author = author.model_dump()
    new_author["id"] = author_id
    AUTHORS[author_id] = new_author

    return new_author

from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator


router = APIRouter(prefix="/products", tags=["Products"])


class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, le=10000)
    category: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        for char in value:
            if not (char.isalnum() or char == " "):
                raise ValueError("Name can contain only letters and numbers")

        return value

    @field_validator("category")
    @classmethod
    def validate_category(cls, value):
        categories = ["Electronics", "Books", "Clothing"]

        if value not in categories:
            raise ValueError("Invalid category")

        return value


@router.post("/")
async def create_product(product: Product):
    return product

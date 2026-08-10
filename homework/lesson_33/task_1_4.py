# 1.
# ✏️ Zadanie 1 – Pierwsze API
# Stwórz aplikację FastAPI z trzema endpoints:
# GET / - zwraca {"message": "Hello"}
# GET /time - zwraca aktualny czas
# GET /random - zwraca losową liczbę 1-100
# (proste)
# 2.
# ✏️ Zadanie 2 – Path Parameters
# Utwórz endpoint GET /greet/{name} który zwraca powitanie dla danej osoby.
# Dodaj walidację: imię musi mieć min 2 znaki.
# (proste)
# 3.
# ✏️ Zadanie 3 – Query Parameters
# Stwórz endpoint GET /calculate który przyjmuje query params:
# a: int (wymagany)
# b: int (wymagany)
# operation: str (domyślnie "add")
# Zwraca wynik operacji: add, subtract, multiply, divide.
# (proste)
# 4.
# ✏️ Zadanie 4 – Pydantic Model
# Zdefiniuj model Product z polami: name, price, quantity.
# Utwórz endpoint POST /products który przyjmuje Product i zwraca go z total_price.
# (proste)




from datetime import datetime
from random import randint

from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, computed_field


app = FastAPI(title="Zadania 1-4")


@app.get("/")
async def hello():
    return {"message": "Hello"}


@app.get("/time")
async def current_time():
    return {"current_time": datetime.now()}


@app.get("/random")
async def random_number():
    return {"number": randint(1, 100)}


@app.get("/greet/{name}")
async def greet(name: str = Path(..., min_length=2)):
    return {"message": f"Hello {name}"}


@app.get("/calculate")
async def calculate(a: int, b: int, operation: str = "add"):
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = a / b
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

    return {"result": result}


class Product(BaseModel):
    name: str
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity


@app.post("/products", response_model=Product, status_code=201)
async def add_product(product: Product):
    return product

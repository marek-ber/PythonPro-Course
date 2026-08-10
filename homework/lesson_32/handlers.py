# 9. 🧠 (Challenge) CRUD API - Produkty (POST): Używając aplikacji z przykładu (z gotową
# integracją SQLAlchemy ):
# 1. Dodaj model Product (z zadania 7) do pliku.
# 2. Pamiętaj o dodaniu go do Base.metadata.create_all .
# 3. Stwórz handler POST na /products , który odczyta name i price z JSON, stworzy
# nowy obiekt Product i zapisze go w bazie.
# 4. Handler powinien zwrócić dane nowego produktu (wraz z ID) i status 201.


# 10. 🧠 (Challenge) CRUD API - Produkty (GET Lista): Bazując na zadaniu 9, stwórz handler
# GET na /products , który pobierze wszystkie produkty z bazy danych ( select(Product) )
# i zwróci je jako listę obiektów JSON


# 11. 🧠 (Challenge) CRUD API - Produkty (GET Pojedynczy): Bazując na zadaniu 10, stwórz
# handler GET na /products/{id} . Handler ma pobrać ID z match_info , znaleźć produkt
# w bazie ( select(Product).where(Product.id == product_id) ). Jeśli produkt istnieje,
# zwróć jego dane JSON. Jeśli nie, podnieś wyjątek web.HTTPNotFound() 


# 14. 🧠 (Challenge) CRUD API - Produkty (PUT/PATCH): Bazując na zadaniu 11, stwórz
# handler PUT (lub PATCH ) na /products/{id} . Handler ma:
# 1. Pobrać produkt (i zwrócić 404, jeśli go nie ma).
# 2. Odczytać nowe dane name i/lub price z await request.json() .
# 3. Zaktualizować atrybuty obiektu produktu.
# 4. Zapisać zmiany w bazie (w ramach sesji i transakcji).
# 5. Zwrócić zaktualizowane dane produktu.

# 15. 🧠 (Challenge) CRUD API - Produkty (DELETE): Bazując na zadaniu 11, stwórz handler
# DELETE na /products/{id} . Handler ma pobrać obiekt, usunąć go ( await
# session.delete(product) ) i zwrócić pustą odpowiedź ze statusem 204 (No Content).


# 16. 🧠 (Challenge) SQLAlchemy Async - Transakcja: (Znacie transakcje). Stwórz dwa
# modele: Account (z polem balance: Mapped[int] ) i handler POST /transfer . Handler
# ma przyjąć JSON { "from_id": 1, "to_id": 2, "amount": 100 } . W ramach jednej
# transakcji ( async with session.begin(): ):
# 1. Pobierz oba konta.
# 2. Sprawdź, czy na koncie from_id jest wystarczająco środków.
# 3. Odejmij amount z from_id i dodaj do to_id .
# 4. Jeśli coś pójdzie nie tak (np. brak środków), transakcja powinna zostać automatycznie
# wycofana (dzięki session.begin() i wyjątkowi).


# 17. 🧠 (Challenge) Aiohttp - Paginacja: (Znacie paginację z Django). Zmodyfikuj handler GET
# /products (zadanie 10). Handler ma przyjmować page (domyślnie 1) i limit (domyślnie 10) z
# request.query. Zmodyfikuj zapytanie SQLAlchemy, aby użyć .offset() i .limit() do zwrócenia
# tylko jednej "strony" wyników.
# Hint: offset = (page - 1) * limit

# 18. 🧠 (Challenge) Aiohttp - Mock API dla AI: Stwórz handler POST na /api/v1/chat .
# Handler ma:
# 1. Oczekiwać JSON-a: {"prompt": "jakaś treść"} .
# 2. Symulować długie przetwarzanie przez AI: await asyncio.sleep(3) .
# 3. Zwrócić odpowiedź JSON: {"response": f"Otrzymałem twój prompt: '{prompt_text}' i
# przetworzyłem go."}.
# (To ćwiczenie pokazuje, jak serwer aiohttp radzi sobie z długimi zadaniami I/O, nie
# blokując innych zapytań).


# 20. 🧠 (Challenge) SQLAlchemy Async - JOIN: (Znacie JOIN). Dodaj do modelu Product
# relację ForeignKey do User (twórca produktu). Zmodyfikuj handler GET
# /products/{id} , aby pobierał produkt wraz z nazwą użytkownika, który go stworzył
# (używając select(Product, User).join(User) lub
# options(joinedload(Product.user)) - opcja dla ambitnych).


import asyncio
from json import JSONDecodeError, dumps

from aiohttp import web
from sqlalchemy import select

from models import Account, Product, User


def json_error(message, status=400):
    return web.Response(
        text=dumps({"error": message}),
        status=status,
        content_type="application/json",
    )


async def add_product(request: web.Request):
    try:
        data = await request.json()
        name = data["name"]
        price = data["price"]
        user_id = data.get("user_id")
    except (JSONDecodeError, KeyError, TypeError):
        raise web.HTTPBadRequest(
            text=dumps({"error": "Podaj name i price"}),
            content_type="application/json",
        )

    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        async with session.begin():
            if user_id is not None:
                user = await session.get(User, user_id)
                if user is None:
                    raise web.HTTPBadRequest(
                        text=dumps({"error": "Nie ma użytkownika o takim ID"}),
                        content_type="application/json",
                    )

            new_product = Product(
                name=name,
                price=price,
                user_id=user_id,
            )
            session.add(new_product)
            await session.flush()
            product = new_product.to_dict()

    return web.json_response(product, status=201)


async def get_all_products(request: web.Request):
    try:
        page = int(request.query.get("page", 1))
        limit = int(request.query.get("limit", 10))
    except ValueError:
        raise web.HTTPBadRequest(
            text=dumps({"error": "page i limit muszą być liczbami"}),
            content_type="application/json",
        )

    if page < 1 or limit < 1:
        raise web.HTTPBadRequest(
            text=dumps({"error": "page i limit muszą być większe od 0"}),
            content_type="application/json",
        )

    offset = (page - 1) * limit

    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        query = select(Product).offset(offset).limit(limit)
        result = await session.execute(query)
        products = result.scalars().all()

    return web.json_response([product.to_dict() for product in products])


async def get_single_product(request: web.Request):
    try:
        product_id = int(request.match_info["id"])
    except ValueError:
        raise web.HTTPBadRequest(
            text=dumps({"error": "Niepoprawne ID produktu"}),
            content_type="application/json",
        )

    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        query = (
            select(Product, User)
            .outerjoin(User, Product.user_id == User.id)
            .where(Product.id == product_id)
        )
        result = await session.execute(query)
        row = result.first()

    if row is None:
        raise web.HTTPNotFound(
            text=dumps({"error": "Nie znaleziono produktu"}),
            content_type="application/json",
        )

    product, user = row
    data = product.to_dict()
    data["created_by"] = user.username if user else None

    return web.json_response(data)


async def update_product(request: web.Request):
    try:
        product_id = int(request.match_info["id"])
    except ValueError:
        raise web.HTTPBadRequest(
            text=dumps({"error": "Niepoprawne ID produktu"}),
            content_type="application/json",
        )

    try:
        data = await request.json()
    except JSONDecodeError:
        raise web.HTTPBadRequest(
            text=dumps({"error": "Niepoprawny JSON"}),
            content_type="application/json",
        )

    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        async with session.begin():
            product = await session.get(Product, product_id)

            if product is None:
                raise web.HTTPNotFound(
                    text=dumps({"error": "Nie znaleziono produktu"}),
                    content_type="application/json",
                )

            if "name" in data:
                product.name = data["name"]

            if "price" in data:
                product.price = data["price"]

            if "user_id" in data:
                user_id = data["user_id"]
                if user_id is not None:
                    user = await session.get(User, user_id)
                    if user is None:
                        raise web.HTTPBadRequest(
                            text=dumps({"error": "Nie ma użytkownika o takim ID"}),
                            content_type="application/json",
                        )
                product.user_id = user_id

            await session.flush()
            updated_product = product.to_dict()

    return web.json_response(updated_product)


async def delete_product(request: web.Request):
    try:
        product_id = int(request.match_info["id"])
    except ValueError:
        raise web.HTTPBadRequest(
            text=dumps({"error": "Niepoprawne ID produktu"}),
            content_type="application/json",
        )

    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        async with session.begin():
            product = await session.get(Product, product_id)

            if product is None:
                raise web.HTTPNotFound(
                    text=dumps({"error": "Nie znaleziono produktu"}),
                    content_type="application/json",
                )

            await session.delete(product)

    return web.Response(status=204)


async def create_user(request: web.Request):
    try:
        data = await request.json()
        username = data["username"]
    except (JSONDecodeError, KeyError):
        raise web.HTTPBadRequest(
            text=dumps({"error": "Podaj username"}),
            content_type="application/json",
        )

    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        async with session.begin():
            query = select(User).where(User.username == username)
            result = await session.execute(query)

            if result.scalar_one_or_none() is not None:
                raise web.HTTPConflict(
                    text=dumps({"error": "Taki użytkownik już istnieje"}),
                    content_type="application/json",
                )

            user = User(username=username)
            session.add(user)
            await session.flush()
            data = user.to_dict()

    return web.json_response(data, status=201)


async def create_account(request: web.Request):
    try:
        data = await request.json()
        balance = int(data.get("balance", 0))
    except (JSONDecodeError, ValueError, TypeError):
        raise web.HTTPBadRequest(
            text=dumps({"error": "Niepoprawny balance"}),
            content_type="application/json",
        )

    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        async with session.begin():
            account = Account(balance=balance)
            session.add(account)
            await session.flush()
            account_data = account.to_dict()

    return web.json_response(account_data, status=201)


async def transfer(request: web.Request):
    try:
        data = await request.json()
        from_id = int(data["from_id"])
        to_id = int(data["to_id"])
        amount = int(data["amount"])
    except (JSONDecodeError, KeyError, ValueError, TypeError):
        raise web.HTTPBadRequest(
            text=dumps({"error": "Podaj from_id, to_id i amount"}),
            content_type="application/json",
        )

    if amount <= 0:
        raise web.HTTPBadRequest(
            text=dumps({"error": "amount musi być większe od 0"}),
            content_type="application/json",
        )

    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        async with session.begin():
            from_account = await session.get(Account, from_id)
            to_account = await session.get(Account, to_id)

            if from_account is None or to_account is None:
                raise web.HTTPNotFound(
                    text=dumps({"error": "Nie znaleziono konta"}),
                    content_type="application/json",
                )

            if from_account.balance < amount:
                raise web.HTTPBadRequest(
                    text=dumps({"error": "Brak wystarczających środków"}),
                    content_type="application/json",
                )

            from_account.balance -= amount
            to_account.balance += amount

    return web.json_response({
        "from_id": from_id,
        "to_id": to_id,
        "amount": amount,
        "status": "OK",
    })


async def chat(request: web.Request):
    try:
        data = await request.json()
        prompt_text = data["prompt"]
    except (JSONDecodeError, KeyError):
        raise web.HTTPBadRequest(
            text=dumps({"error": "Podaj prompt"}),
            content_type="application/json",
        )

    await asyncio.sleep(3)

    return web.json_response({
        "response": f"Otrzymałem twój prompt: '{prompt_text}' i przetworzyłem go."
    })

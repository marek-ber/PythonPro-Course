import os

from aiohttp import web
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from models import Base
from routes import setup_routes


load_dotenv()

DB_URL = os.getenv(
    "DB_URL",
    "postgresql+asyncpg://postgres:postgres@localhost/aio_test_db",
)


async def init_db(app: web.Application):
    print(f"Inicjalizuję połączenie z bazą danych: {DB_URL}")

    engine = create_async_engine(DB_URL, echo=True)

    session_factory = async_sessionmaker(
        engine,
        expire_on_commit=False,
        class_=AsyncSession,
    )

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    app["db_engine"] = engine
    app["db_session_factory"] = session_factory

    print("Połączenie z bazą danych gotowe.")


async def close_db(app: web.Application):
    print("Zamykam pulę połączeń z bazą danych.")
    await app["db_engine"].dispose()


def create_app():
    app = web.Application()

    setup_routes(app)

    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)

    return app


if __name__ == "__main__":
    app = create_app()
    print("--- Start serwera na http://127.0.0.1:8080 ---")
    print(f"--- Baza danych: {DB_URL} ---")
    web.run_app(app, host="127.0.0.1", port=8080)

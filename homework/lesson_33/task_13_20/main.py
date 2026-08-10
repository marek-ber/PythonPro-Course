import json
import logging
import time
import uuid
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from database import close_db, init_db
from routers import blog, books


BASE_DIR = Path(__file__).resolve().parent
CACHE_FILE = BASE_DIR / "cache.json"

logging.basicConfig(
    filename=BASE_DIR / "requests.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s",
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()

    if CACHE_FILE.exists():
        with open(CACHE_FILE, "r", encoding="utf-8") as file:
            app.state.cache = json.load(file)
    else:
        app.state.cache = {}

    yield

    with open(CACHE_FILE, "w", encoding="utf-8") as file:
        json.dump(app.state.cache, file, ensure_ascii=False, indent=2)

    await close_db()


app = FastAPI(
    title="Lesson 33 FastAPI",
    description="Zadania 13-20",
    lifespan=lifespan,
)


@app.middleware("http")
async def request_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())
    start = time.perf_counter()

    if request.method in ["POST", "PUT", "PATCH"]:
        body = await request.body()
        text = body.decode("utf-8", errors="ignore").lower()
        blocked_words = ["cholera", "idiota"]

        if any(word in text for word in blocked_words):
            return JSONResponse(
                status_code=400,
                content={"detail": "Content rejected by moderation"},
            )

    response = await call_next(request)
    process_time = time.perf_counter() - start

    logging.info(
        "%s %s %.4fs %s",
        request.method,
        request.url.path,
        process_time,
        request_id,
    )

    response.headers["X-Request-ID"] = request_id
    return response


app.include_router(books.router)
app.include_router(blog.router)


@app.get("/")
async def root():
    return {"message": "Lesson 33 API"}

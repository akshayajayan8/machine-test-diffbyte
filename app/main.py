from fastapi import FastAPI

from contextlib import asynccontextmanager

from app.models import Base
from app.database import engine
from app.routes import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    await engine.dispose()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def hello():
    return {"status:running"}

app.include_router(router=router, prefix="/api/v1")


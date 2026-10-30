from fastapi import FastAPI

from contextlib import asynccontextmanager

from app.models import Base
from app.database import engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create all tables on startup
    Base.metadata.create_all(bind=engine)
    yield
    # Code here runs on shutdown (if needed)

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def hello():
    return {"status:running"}


from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from app.config import settings

DATABASE_URL = "sqlite+aiosqlite:///project.db"
engine = create_async_engine(DATABASE_URL)

SessionLocal = AsyncSession(
    bind=engine
)

async def get_db():
    session =await SessionLocal()
    try:
        yield session
    finally:
        await session.close()
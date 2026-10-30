from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import User
from app.schemas import UserCreate

router = APIRouter()

#define endpoint
@router.post("/user")
async def create_user(
    body: UserCreate,
    db:AsyncSession = Depends(get_db)
):
    user = User(
        name = body.name,
        email = body.email,
        message = body.message
    )

    db.add(user)
    await db.commit()
    return JSONResponse(
        status_code=201,
        content={
            "id":str(user.id),
        }
    )
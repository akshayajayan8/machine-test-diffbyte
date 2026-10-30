from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import Column, String
from sqlalchemy import UUID
import uuid

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):

    __tablename__ = "users"

    id = Column(UUID,index=True, primary_key=True, default=uuid.uuid4)
    name = Column(String(200))
    email = Column(String(200))
    message = Column(String(500))
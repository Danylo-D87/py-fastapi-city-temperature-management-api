from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine

from app.core import config


SQLALCHEMY_DATABASE_URL = config.SQLALCHEMY_DATABASE_URL

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

Base = declarative_base()

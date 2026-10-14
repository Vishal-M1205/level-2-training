from fastapi import Request
from app.core.config import config
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.pool import AsyncAdaptedQueuePool
from sqlalchemy import URL

conn_url = URL.create(
    drivername="postgresql+psycopg",
    username="postgres",
    password="CG-vak123",
    host="localhost",
    database="student_db",
    port=5432,
)


async_engine = create_async_engine(
    url=conn_url, poolclass=AsyncAdaptedQueuePool, pool_size=3, max_overflow=10
)

AsyncSessionContext = async_sessionmaker(bind=async_engine, expire_on_commit=False)


async def get_db_connection() -> AsyncGenerator[AsyncSession, None]:

    async with AsyncSessionContext() as session:
        yield session

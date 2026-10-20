import pytest
import psycopg
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.pool import NullPool
from app.models.base import Base

from app.main import app
from app.database import conn_url, get_db_connection
from app.core.config import config

test_conn_url = conn_url.set(database="student_db_test")
test_engine = create_async_engine(test_conn_url, poolclass=NullPool)
TestingSessionLocal = async_sessionmaker(bind=test_engine, expire_on_commit=False)


async def override_get_db_connection():
    async with TestingSessionLocal() as session:
        yield session


@pytest.fixture
def client():
    """dependency_overrides is a dictionary , as get_db_connection used in the app we are overriding and clear() the
    dict at last"""
    app.dependency_overrides[get_db_connection] = override_get_db_connection
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture(autouse=True)
def clean_tables():
    """autouse run automattically , first the yeild means it let all the fixturre and test to run ,
    RESTART IDENTITY , the id starts frm 1 , CASCADE prevents the error occur from the refrential rows
    """
    yield
    with psycopg.connect(
        host=config.database_host,
        port=config.database_port,
        user=config.database_user,
        password=config.database_password,
        dbname="student_db_test",
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "TRUNCATE TABLE exam_marks, id_cards, students, subjects RESTART IDENTITY CASCADE;"
            )
        conn.commit()

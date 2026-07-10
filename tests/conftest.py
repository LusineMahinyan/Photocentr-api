import pytest_asyncio

from httpx import AsyncClient, ASGITransport

from app.main import app
from app.db.database import get_db, async_session


@pytest_asyncio.fixture
async def client():

    async def override_get_db():
        async with async_session() as session:
            yield session

    app.dependency_overrides[get_db] = override_get_db

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        yield client

    app.dependency_overrides.clear()

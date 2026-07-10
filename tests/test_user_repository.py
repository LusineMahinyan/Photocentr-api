import pytest
from unittest.mock import AsyncMock, MagicMock

from app.repositories.user_repository import UserRepository


class FakeResult:

    def scalar_one_or_none(self):
        return "user"


@pytest.mark.asyncio
async def test_get_by_email():

    db = MagicMock()

    db.execute = AsyncMock(return_value=FakeResult())

    repo = UserRepository(db)

    result = await repo.get_by_email("test@test.com")

    assert result == "user"


@pytest.mark.asyncio
async def test_get_by_phone():

    db = MagicMock()

    db.execute = AsyncMock(return_value=FakeResult())

    repo = UserRepository(db)

    result = await repo.get_by_phone("+79999999999")

    assert result == "user"


@pytest.mark.asyncio
async def test_get_by_id():

    db = MagicMock()

    db.execute = AsyncMock(return_value=FakeResult())

    repo = UserRepository(db)

    result = await repo.get_by_id(1)

    assert result == "user"


@pytest.mark.asyncio
async def test_create_user():

    db = MagicMock()

    db.commit = AsyncMock()
    db.refresh = AsyncMock()

    repo = UserRepository(db)

    result = await repo.create(
        {
            "email": "test@test.com",
            "phone": "+79999999999",
            "full_name": "Test",
            "hashed_password": "hash",
        }
    )

    assert result.email == "test@test.com"
    db.commit.assert_awaited_once()
    db.refresh.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_by_email_or_phone():

    db = MagicMock()

    db.execute = AsyncMock(return_value=FakeResult())

    repo = UserRepository(db)

    result = await repo.get_by_email_or_phone("test@test.com")

    assert result == "user"

import pytest
from unittest.mock import AsyncMock

from fastapi import HTTPException

from app.services.user_service import UserService
from app.schemas.user import UserCreate


@pytest.fixture
def repository():
    repo = AsyncMock()
    return repo


@pytest.fixture
def service(repository):
    return UserService(repository)


@pytest.fixture
def user_data():
    return UserCreate(
        full_name="Иван Иванов",
        email="ivan@test.com",
        phone="+79991234567",
        password="Password1!",
        confirm_password="Password1!",
    )


@pytest.mark.asyncio
async def test_register_success(service, repository, user_data):
    repository.get_by_email.return_value = None
    repository.get_by_phone.return_value = None
    repository.create.return_value = {"id": 1, "email": user_data.email}

    result = await service.register(user_data)

    repository.create.assert_called_once()
    assert result["email"] == user_data.email


@pytest.mark.asyncio
async def test_register_existing_email(service, repository, user_data):
    repository.get_by_email.return_value = object()

    with pytest.raises(HTTPException) as exc:
        await service.register(user_data)

    assert exc.value.status_code == 400
    assert exc.value.detail == "Email already registered"


@pytest.mark.asyncio
async def test_register_existing_phone(service, repository, user_data):
    repository.get_by_email.return_value = None
    repository.get_by_phone.return_value = object()

    with pytest.raises(HTTPException) as exc:
        await service.register(user_data)

    assert exc.value.status_code == 400
    assert exc.value.detail == "Phone already registered"


@pytest.mark.asyncio
async def test_login_user_not_found(service, repository):
    repository.get_by_email_or_phone.return_value = None

    with pytest.raises(HTTPException) as exc:
        await service.login("ivan@test.com", "Password1!")

    assert exc.value.status_code == 401

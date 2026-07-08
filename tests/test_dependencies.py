import pytest
from unittest.mock import AsyncMock, patch

from fastapi import HTTPException

from app.core.dependencies import (
    get_current_user,
    require_admin,
    get_current_admin
)


class FakeUser:
    id = 1
    is_admin = True


class FakeUserNotAdmin:
    id = 1
    is_admin = False


@pytest.mark.asyncio
async def test_get_current_user_success():

    token = "valid_token"

    with patch(
        "app.core.dependencies.jwt.decode",
        return_value={"sub": "1"}
    ):

        with patch(
            "app.core.dependencies.UserRepository"
        ) as repo:

            repo.return_value.get_by_id = AsyncMock(
                return_value=FakeUser()
            )

            result = await get_current_user(
                token=token,
                db="test_db"
            )

            assert result.id == 1


@pytest.mark.asyncio
async def test_get_current_user_without_sub():

    with patch(
        "app.core.dependencies.jwt.decode",
        return_value={}
    ):

        with pytest.raises(HTTPException) as exc:

            await get_current_user(
                token="token",
                db="db"
            )

        assert exc.value.status_code == 401


@pytest.mark.asyncio
async def test_get_current_user_invalid_token():

    from jose import JWTError

    with patch(
        "app.core.dependencies.jwt.decode",
        side_effect=JWTError()
    ):

        with pytest.raises(HTTPException):

            await get_current_user(
                token="bad",
                db="db"
            )


@pytest.mark.asyncio
async def test_get_current_user_not_found():

    with patch(
        "app.core.dependencies.jwt.decode",
        return_value={"sub": "1"}
    ):

        with patch(
            "app.core.dependencies.UserRepository"
        ) as repo:

            repo.return_value.get_by_id = AsyncMock(
                return_value=None
            )

            with pytest.raises(HTTPException):

                await get_current_user(
                    token="token",
                    db="db"
                )


@pytest.mark.asyncio
async def test_require_admin_success():

    user = FakeUser()

    result = await require_admin(user)

    assert result == user


@pytest.mark.asyncio
async def test_require_admin_fail():

    user = FakeUserNotAdmin()

    with pytest.raises(HTTPException):

        await require_admin(user)


@pytest.mark.asyncio
async def test_get_current_admin_fail():

    user = FakeUserNotAdmin()

    with pytest.raises(HTTPException):

        await get_current_admin(user)

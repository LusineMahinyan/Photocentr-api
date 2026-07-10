import pytest

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)
from jose import jwt
from app.core.config import settings


def test_hash_password():
    password = "Password1!"

    hashed = hash_password(password)

    assert hashed != password
    assert isinstance(hashed, str)


def test_verify_password_success():
    password = "Password1!"

    hashed = hash_password(password)

    result = verify_password(
        password,
        hashed,
    )

    assert result is True


def test_verify_password_wrong_password():
    password = "Password1!"

    hashed = hash_password(password)

    result = verify_password(
        "WrongPassword",
        hashed,
    )

    assert result is False


def test_create_access_token():
    data = {"sub": "1"}

    token = create_access_token(data)

    assert isinstance(token, str)

    payload = jwt.decode(
        token,
        settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM],
    )

    assert payload["sub"] == "1"
    assert "exp" in payload

import pytest
import uuid
import random


@pytest.mark.asyncio
async def test_register_user(client):
    email = f"{uuid.uuid4().hex}@test.com"
    phone = f"+79{random.randint(100000000, 999999999)}"

    response = await client.post(
        "/api/v1/users/register",
        json={
            "full_name": "Иван Иванов",
            "email": email,
            "phone": phone,
            "password": "Password1!",
            "confirm_password": "Password1!",
        },
    )

    assert response.status_code == 201

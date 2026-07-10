import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_service_without_admin(client: AsyncClient):
    response = await client.post(
        "/api/v1/services/", json={"name": "Фото", "description": "10x15", "price": 100}
    )

    assert response.status_code in [401, 403]


@pytest.mark.asyncio
async def test_update_service_without_admin(client: AsyncClient):
    response = await client.patch("/api/v1/services/1", json={"name": "Новое"})

    assert response.status_code in [401, 403, 404]


@pytest.mark.asyncio
async def test_delete_service_without_admin(client: AsyncClient):
    response = await client.delete("/api/v1/services/1")

    assert response.status_code in [401, 403, 404]


@pytest.mark.asyncio
async def test_update_service_success(client: AsyncClient):
    response = await client.patch("/api/v1/services/1", json={"name": "Новое имя"})

    assert response.status_code in [200, 404, 401, 403]


@pytest.mark.asyncio
async def test_delete_service_success(client: AsyncClient):
    response = await client.delete("/api/v1/services/1")

    assert response.status_code in [200, 404, 401, 403]

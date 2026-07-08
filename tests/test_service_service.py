import pytest
from unittest.mock import AsyncMock

from app.services.service_service import ServiceService


@pytest.mark.asyncio
async def test_get_all_active():
    repository = AsyncMock()
    repository.get_all_active.return_value = ["service1", "service2"]

    service = ServiceService(repository)

    result = await service.get_all_active()

    assert result == ["service1", "service2"]
    repository.get_all_active.assert_awaited_once()


@pytest.mark.asyncio
async def test_create_service():
    repository = AsyncMock()
    service_data = AsyncMock()

    repository.create.return_value = {"id": 1}

    service = ServiceService(repository)

    result = await service.create(service_data)

    assert result == {"id": 1}
    repository.create.assert_awaited_once_with(service_data)


@pytest.mark.asyncio
async def test_update_service_not_found():
    repository = AsyncMock()

    repository.get_by_id.return_value = None

    service = ServiceService(repository)

    result = await service.update(1, AsyncMock())

    assert result is None
    repository.update.assert_not_called()


@pytest.mark.asyncio
async def test_update_service_success():
    repository = AsyncMock()

    existing = object()
    service_data = AsyncMock()

    repository.get_by_id.return_value = existing
    repository.update.return_value = {"id": 1}

    service = ServiceService(repository)

    result = await service.update(1, service_data)

    assert result == {"id": 1}
    repository.get_by_id.assert_awaited_once_with(1)
    repository.update.assert_awaited_once_with(existing, service_data)


@pytest.mark.asyncio
async def test_delete_service_not_found():
    repository = AsyncMock()

    repository.get_by_id.return_value = None

    service = ServiceService(repository)

    result = await service.delete(1)

    assert result is None
    repository.delete.assert_not_called()


@pytest.mark.asyncio
async def test_delete_service_success():
    repository = AsyncMock()

    existing = object()

    repository.get_by_id.return_value = existing
    repository.delete.return_value = True

    service = ServiceService(repository)

    result = await service.delete(1)

    assert result is True
    repository.get_by_id.assert_awaited_once_with(1)
    repository.delete.assert_awaited_once_with(existing)

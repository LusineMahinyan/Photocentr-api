import pytest
from unittest.mock import AsyncMock

from app.services.order_service import OrderService


@pytest.fixture
def repository():
    return AsyncMock()


@pytest.fixture
def service(repository):
    return OrderService(repository)


@pytest.mark.asyncio
async def test_create_order(service, repository):

    order_data = AsyncMock()
    order_data.service_ids = [1, 2]

    repository.create.return_value = {"id": 1}

    result = await service.create_order(user_id=1, order_data=order_data)

    repository.create.assert_called_once_with(1, [1, 2])

    assert result == {"id": 1}


@pytest.mark.asyncio
async def test_get_my_orders(service, repository):

    repository.get_user_orders.return_value = [{"id": 1}, {"id": 2}]

    result = await service.get_my_orders(1)

    repository.get_user_orders.assert_called_once_with(1)

    assert len(result) == 2


@pytest.mark.asyncio
async def test_get_order_not_found(service, repository):

    repository.get_by_id.return_value = None

    result = await service.get_order(1)

    assert result is None


@pytest.mark.asyncio
async def test_get_order_success(service, repository):

    order = AsyncMock()
    order.user_id = 1

    repository.get_by_id.return_value = order

    result = await service.get_order(1)

    assert result == order


@pytest.mark.asyncio
async def test_get_order_wrong_user(service, repository):

    order = AsyncMock()
    order.user_id = 2

    repository.get_by_id.return_value = order

    result = await service.get_order(order_id=1, user_id=1)

    assert result is None


@pytest.mark.asyncio
async def test_get_order_owner(service, repository):

    order = AsyncMock()
    order.user_id = 1

    repository.get_by_id.return_value = order

    result = await service.get_order(order_id=1, user_id=1)

    assert result == order


@pytest.mark.asyncio
async def test_get_all_orders(service, repository):

    repository.get_all.return_value = [{"id": 1}, {"id": 2}]

    result = await service.get_all_orders()

    repository.get_all.assert_called_once()

    assert len(result) == 2


@pytest.mark.asyncio
async def test_update_status_order_not_found(service, repository):

    status_data = AsyncMock()
    status_data.status = "completed"

    repository.get_by_id.return_value = None

    result = await service.update_status(1, status_data)

    assert result is None


@pytest.mark.asyncio
async def test_update_status_success(service, repository):

    order = AsyncMock()

    status_data = AsyncMock()
    status_data.status = "completed"

    repository.get_by_id.return_value = order

    repository.update_status.return_value = order

    result = await service.update_status(1, status_data)

    repository.update_status.assert_called_once_with(order, "completed")

    assert result == order

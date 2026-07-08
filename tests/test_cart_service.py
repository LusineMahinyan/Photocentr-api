import pytest
from unittest.mock import AsyncMock

from app.services.cart_service import CartService


@pytest.fixture
def cart_repository():
    return AsyncMock()


@pytest.fixture
def order_repository():
    return AsyncMock()


@pytest.fixture
def service(cart_repository, order_repository):
    return CartService(cart_repository, order_repository)


@pytest.mark.asyncio
async def test_add_service(service, cart_repository):
    cart_repository.add_service.return_value = True

    result = await service.add_service(1, 2)

    cart_repository.add_service.assert_called_once_with(1, 2)
    assert result is True


@pytest.mark.asyncio
async def test_get_empty_cart(service, cart_repository):
    cart_repository.get_by_user_id.return_value = None

    result = await service.get_cart(1)

    assert result == {
        "items": [],
        "total_price": 0
    }


@pytest.mark.asyncio
async def test_remove_item(service, cart_repository):
    cart_repository.remove_item.return_value = True

    result = await service.remove_item(1, 5)

    cart_repository.remove_item.assert_called_once_with(1, 5)
    assert result is True


@pytest.mark.asyncio
async def test_clear_cart(service, cart_repository):
    cart_repository.clear_cart.return_value = True

    result = await service.clear_cart(1)

    cart_repository.clear_cart.assert_called_once_with(1)
    assert result is True


@pytest.mark.asyncio
async def test_checkout_empty_cart(service, cart_repository):
    cart_repository.get_by_user_id.return_value = None

    result = await service.checkout(1)

    assert result is None


@pytest.mark.asyncio
async def test_checkout_success(service, cart_repository, order_repository):
    cart = AsyncMock()
    cart.items = [object()]

    order = {"id": 1}

    cart_repository.get_by_user_id.return_value = cart
    order_repository.create_from_cart.return_value = order

    result = await service.checkout(1)

    order_repository.create_from_cart.assert_called_once_with(1, cart)
    cart_repository.clear_cart.assert_called_once_with(1)

    assert result == order


@pytest.mark.asyncio
async def test_get_cart_with_items(service, cart_repository):
    service1 = AsyncMock()
    service1.price = 100

    item1 = AsyncMock()
    item1.service = service1
    item1.service_id = 1
    item1.quantity = 2

    service2 = AsyncMock()
    service2.price = 50

    item2 = AsyncMock()
    item2.service = service2
    item2.service_id = 2
    item2.quantity = 1

    cart = AsyncMock()
    cart.items = [item1, item2]

    cart_repository.get_by_user_id.return_value = cart

    result = await service.get_cart(1)

    assert result["total_price"] == 250
    assert len(result["items"]) == 2
    assert result["items"][0]["service_id"] == 1
    assert result["items"][0]["quantity"] == 2

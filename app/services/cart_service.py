from app.repositories.cart_repository import CartRepository
from app.repositories.order_repository import OrderRepository


class CartService:

    def __init__(
        self,
        cart_repository: CartRepository,
        order_repository: OrderRepository | None = None,
    ):
        self.cart_repository = cart_repository
        self.order_repository = order_repository

    async def add_service(self, user_id: int, service_id: int):
        return await self.cart_repository.add_service(user_id, service_id)

    async def get_cart(self, user_id: int):

        cart = await self.cart_repository.get_by_user_id(user_id)

        if not cart:
            return {"items": [], "total_price": 0}

        items = []

        total_price = 0

        for item in cart.items:
            price = item.service.price

            items.append(
                {
                    "id": item.id,
                    "service_id": item.service_id,
                    "quantity": item.quantity,
                    "price": price,
                }
            )

            total_price += price * item.quantity

        return {"items": items, "total_price": total_price}

    async def remove_item(self, user_id: int, item_id: int):
        return await self.cart_repository.remove_item(user_id, item_id)

    async def checkout(self, user_id: int):

        cart = await self.cart_repository.get_by_user_id(user_id)

        if not cart or not cart.items:
            return None

        order = await self.order_repository.create_from_cart(user_id, cart)

        await self.cart_repository.clear_cart(user_id)

        return order

    async def clear_cart(self, user_id: int):
        return await self.cart_repository.clear_cart(user_id)

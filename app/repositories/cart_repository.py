from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.service import Service


class CartRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_user_id(
            self,
            user_id: int
    ):

        result = await self.db.execute(
            select(Cart)
            .where(
                Cart.user_id == user_id
            )
            .options(
                selectinload(Cart.items).selectinload(CartItem.service)
            )
        )

        return result.scalar_one_or_none()

    async def create_cart(
        self,
        user_id: int
    ):

        cart = Cart(
            user_id=user_id
        )

        self.db.add(cart)

        await self.db.commit()

        await self.db.refresh(cart)

        return cart

    async def add_service(
            self,
            user_id: int,
            service_id: int
    ):

        cart = await self.get_by_user_id(
            user_id
        )

        if not cart:
            cart = await self.create_cart(
                user_id
            )

        service = await self.db.get(
            Service,
            service_id
        )

        if not service:
            return None

        item_result = await self.db.execute(
            select(CartItem).where(
                CartItem.cart_id == cart.id,
                CartItem.service_id == service_id
            )
        )

        cart_item = item_result.scalar_one_or_none()

        if cart_item:
            cart_item.quantity += 1

        else:
            cart_item = CartItem(
                cart_id=cart.id,
                service_id=service_id,
                quantity=1
            )

            self.db.add(cart_item)

        await self.db.commit()

        await self.db.refresh(cart_item)

        return cart_item

    async def remove_item(
            self,
            user_id: int,
            item_id: int
    ):

        cart = await self.get_by_user_id(
            user_id
        )

        if not cart:
            return False

        item = None

        for cart_item in cart.items:
            if cart_item.id == item_id:
                item = cart_item
                break

        if not item:
            return False

        await self.db.delete(item)
        await self.db.commit()

        return True

    async def clear_cart(
            self,
            user_id: int
    ):

        cart = await self.get_by_user_id(
            user_id
        )

        if not cart:
            return False

        for item in cart.items:
            await self.db.delete(item)

        await self.db.commit()

        return True

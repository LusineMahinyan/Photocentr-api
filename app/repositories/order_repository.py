from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.service import Service


class OrderRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, user_id: int, service_ids: list[int]):

        result = await self.db.execute(
            select(Service).where(
                Service.id.in_(service_ids), Service.is_active.is_(True)
            )
        )

        services = result.scalars().all()

        if not services:
            return None

        total_price = sum(service.price for service in services)

        order = Order(user_id=user_id, total_price=total_price, status="new")

        self.db.add(order)

        await self.db.flush()

        for service in services:
            item = OrderItem(
                order_id=order.id,
                service_id=service.id,
                quantity=1,
                price=service.price,
            )

            self.db.add(item)

        await self.db.commit()
        await self.db.refresh(order)

        return order

    async def get_by_id(self, order_id: int):

        result = await self.db.execute(
            select(Order).options(selectinload(Order.items)).where(Order.id == order_id)
        )

        return result.scalar_one_or_none()

    async def get_user_orders(self, user_id: int):

        result = await self.db.execute(
            select(Order)
            .options(selectinload(Order.items))
            .where(Order.user_id == user_id)
        )

        return result.scalars().all()

    async def get_all(self):

        result = await self.db.execute(select(Order).options(selectinload(Order.items)))

        return result.scalars().all()

    async def update_status(self, order: Order, status: str):

        order.status = status

        await self.db.commit()
        await self.db.refresh(order)

        return order

    async def create_from_cart(self, user_id: int, cart):

        total_price = 0

        order = Order(user_id=user_id, total_price=0, status="new")

        self.db.add(order)

        await self.db.flush()

        for cart_item in cart.items:
            price = cart_item.service.price

            total_price += price * cart_item.quantity

            order_item = OrderItem(
                order_id=order.id,
                service_id=cart_item.service_id,
                quantity=cart_item.quantity,
                price=price,
            )

            self.db.add(order_item)

        order.total_price = total_price

        await self.db.commit()

        result = await self.db.execute(
            select(Order).options(selectinload(Order.items)).where(Order.id == order.id)
        )

        return result.scalar_one()

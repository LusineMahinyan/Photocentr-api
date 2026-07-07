from app.repositories.order_repository import OrderRepository
from app.schemas.order import OrderCreate, OrderStatusUpdate


class OrderService:

    def __init__(self, repository: OrderRepository):
        self.repository = repository


    async def create_order(
            self,
            user_id: int,
            order_data: OrderCreate
    ):
        return await self.repository.create(
            user_id,
            order_data.service_ids
        )


    async def get_my_orders(
            self,
            user_id: int
    ):
        return await self.repository.get_user_orders(
            user_id
        )


    async def get_order(
            self,
            order_id: int
    ):
        return await self.repository.get_by_id(
            order_id
        )


    async def get_all_orders(self):
        return await self.repository.get_all()


    async def update_status(
            self,
            order_id: int,
            status_data: OrderStatusUpdate
    ):

        order = await self.repository.get_by_id(
            order_id
        )

        if not order:
            return None

        return await self.repository.update_status(
            order,
            status_data.status
        )

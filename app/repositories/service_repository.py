from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.service import Service
from app.schemas.service import ServiceCreate, ServiceUpdate


class ServiceRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_active(self):
        result = await self.db.execute(
            select(Service).where(Service.is_active.is_(True))
        )

        return result.scalars().all()

    async def get_by_id(self, service_id: int):
        result = await self.db.execute(select(Service).where(Service.id == service_id))

        return result.scalar_one_or_none()

    async def create(self, service_data: ServiceCreate):

        service = Service(
            name=service_data.name,
            description=service_data.description,
            price=service_data.price,
        )

        self.db.add(service)

        await self.db.commit()
        await self.db.refresh(service)

        return service

    async def update(self, service: Service, service_data: ServiceUpdate):

        data = service_data.model_dump(exclude_unset=True)

        for key, value in data.items():
            setattr(service, key, value)

        await self.db.commit()
        await self.db.refresh(service)

        return service

    async def delete(self, service: Service):
        service.is_active = False

        await self.db.commit()

        return service

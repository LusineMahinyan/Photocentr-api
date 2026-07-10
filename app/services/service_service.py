from app.repositories.service_repository import ServiceRepository
from app.schemas.service import ServiceCreate, ServiceUpdate


class ServiceService:

    def __init__(self, repository: ServiceRepository):
        self.repository = repository

    async def get_all_active(self):
        return await self.repository.get_all_active()

    async def create(self, service_data: ServiceCreate):
        return await self.repository.create(service_data)

    async def update(self, service_id: int, service_data: ServiceUpdate):
        service = await self.repository.get_by_id(service_id)

        if not service:
            return None

        return await self.repository.update(service, service_data)

    async def delete(self, service_id: int):
        service = await self.repository.get_by_id(service_id)

        if not service:
            return None

        return await self.repository.delete(service)

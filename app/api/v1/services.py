from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.repositories.service_repository import ServiceRepository
from app.schemas.service import (
    ServiceCreate,
    ServiceUpdate,
    ServiceResponse
)
from app.services.service_service import ServiceService
from app.core.dependencies import require_admin



router = APIRouter(
    prefix="/services",
    tags=["Services"]
)


@router.get(
    "/",
    response_model=list[ServiceResponse]
)
async def get_services(
    db: AsyncSession = Depends(get_db)
):
    repository = ServiceRepository(db)
    service = ServiceService(repository)

    return await service.get_all_active()


@router.post(
    "/",
    response_model=ServiceResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_admin)]
)

async def create_service(
    service_data: ServiceCreate,
    db: AsyncSession = Depends(get_db)
):
    repository = ServiceRepository(db)
    service = ServiceService(repository)

    return await service.create(service_data)


@router.patch(
    "/{service_id}",
    response_model=ServiceResponse,
    dependencies=[Depends(require_admin)]
)

async def update_service(
    service_id: int,
    service_data: ServiceUpdate,
    db: AsyncSession = Depends(get_db)
):
    repository = ServiceRepository(db)
    service = ServiceService(repository)

    updated_service = await service.update(
        service_id,
        service_data
    )

    if not updated_service:
        raise HTTPException(
            status_code=404,
            detail="Услуга не найдена"
        )

    return updated_service


@router.delete(
    "/{service_id}",
    dependencies=[Depends(require_admin)]
)

async def delete_service(
    service_id: int,
    db: AsyncSession = Depends(get_db)
):
    repository = ServiceRepository(db)
    service = ServiceService(repository)

    deleted_service = await service.delete(service_id)

    if not deleted_service:
        raise HTTPException(
            status_code=404,
            detail="Услуга не найдена"
        )

    return {
        "message": "Услуга успешно удалена"
    }

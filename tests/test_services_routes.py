import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from app.api.v1.services import (
    get_services,
    create_service,
    update_service,
    delete_service
)

from app.schemas.service import ServiceCreate, ServiceUpdate


@pytest.mark.asyncio
async def test_get_services_route():

    with patch(
        "app.api.v1.services.ServiceRepository"
    ) as repo:

        repo.return_value.get_all_active = AsyncMock(
            return_value=[]
        )

        result = await get_services(
            current_user=MagicMock(),
            db=MagicMock()
        )

        assert result == []


@pytest.mark.asyncio
async def test_create_service_route():

    data = ServiceCreate(
        name="Фото",
        description="10x15",
        price=100
    )

    with patch(
        "app.api.v1.services.ServiceRepository"
    ) as repo:

        repo.return_value.create = AsyncMock(
            return_value=data
        )

        result = await create_service(
            service_data=data,
            db=MagicMock()
        )

        assert result == data


@pytest.mark.asyncio
async def test_update_service_not_found_route():

    with patch(
        "app.api.v1.services.ServiceRepository"
    ) as repo:

        repo.return_value.get_by_id = AsyncMock(
            return_value=None
        )

        with pytest.raises(Exception):

            await update_service(
                service_id=999,
                service_data=ServiceUpdate(
                    name="test"
                ),
                db=MagicMock()
            )


@pytest.mark.asyncio
async def test_delete_service_not_found_route():

    with patch(
        "app.api.v1.services.ServiceRepository"
    ) as repo:

        repo.return_value.get_by_id = AsyncMock(
            return_value=None
        )

        with pytest.raises(Exception):

            await delete_service(
                service_id=999,
                db=MagicMock()
            )

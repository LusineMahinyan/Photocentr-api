from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserOut
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "/register",
    response_model=UserOut,
    status_code=201,
)
async def register_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    repository = UserRepository(db)
    service = UserService(repository)

    return await service.register(user_data)

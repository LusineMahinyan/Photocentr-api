from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user import UserCreate, UserOut
from app.services.user import UserService
from app.db.session import get_session

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserOut)
async def register(user: UserCreate, session: AsyncSession = Depends(get_session)):
    service = UserService()

    try:
        new_user = await service.register_user(session, user)
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

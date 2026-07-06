from fastapi import HTTPException, status

from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def register(self, user_data: UserCreate) -> User:
        existing_email = await self.repository.get_by_email(user_data.email)
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

        existing_phone = await self.repository.get_by_phone(user_data.phone)
        if existing_phone:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Phone already registered",
            )

        user = User(
            full_name=user_data.full_name,
            email=user_data.email,
            phone=user_data.phone,
            hashed_password=hash_password(user_data.password),
        )

        return await self.repository.create(user)

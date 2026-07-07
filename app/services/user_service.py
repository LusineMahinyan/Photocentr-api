from fastapi import HTTPException, status

from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.core.security import verify_password, create_access_token


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

        user_dict = {
            "full_name": user_data.full_name,
            "email": user_data.email,
            "phone": user_data.phone,
            "hashed_password": hash_password(user_data.password),
        }

        return await self.repository.create(user_dict)

    async def login(self, identifier: str, password: str):
        user = await self.repository.get_by_email_or_phone(identifier)

        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        if not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        token = create_access_token(
            data={"sub": str(user.id)}
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }

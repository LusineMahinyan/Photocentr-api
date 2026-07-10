from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select

from app.models.user import User


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_email(self, email: str) -> User | None:
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def get_by_phone(self, phone: str) -> User | None:
        result = await self.db.execute(select(User).where(User.phone == phone))
        return result.scalar_one_or_none()

    async def get_by_email_or_phone(self, identifier: str):
        from sqlalchemy import select
        from app.models.user import User

        query = select(User).where(
            (User.email == identifier) | (User.phone == identifier)
        )

        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def get_by_id(self, user_id: int):
        from sqlalchemy import select
        from app.models.user import User

        result = await self.db.execute(select(User).where(User.id == user_id))

        return result.scalar_one_or_none()

    async def create(self, data: dict):
        user = User(**data)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

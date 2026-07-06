from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User


class UserRepository:

    async def get_by_email(self, session: AsyncSession, email: str):
        result = await session.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def get_by_phone(self, session: AsyncSession, phone: str):
        result = await session.execute(
            select(User).where(User.phone == phone)
        )
        return result.scalar_one_or_none()

    async def create(self, session: AsyncSession, full_name: str, email: str, phone: str, hashed_password: str):
        user = User(
            full_name=full_name,
            email=email,
            phone=phone,
            hashed_password=hashed_password
        )

        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user

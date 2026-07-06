from app.repositories.user import UserRepository
from app.core.security import hash_password


class UserService:

    def __init__(self):
        self.repo = UserRepository()

    async def register_user(self, session, data):
        existing_email = await self.repo.get_by_email(session, data.email)
        if existing_email:
            raise ValueError("Email already exists")

        existing_phone = await self.repo.get_by_phone(session, data.phone)
        if existing_phone:
            raise ValueError("Phone already exists")

        user = await self.repo.create(
            session=session,
            full_name=data.full_name,
            email=data.email,
            phone=data.phone,
            hashed_password=hash_password(data.password)
        )

        return user

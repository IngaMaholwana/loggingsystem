from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from app.models.user import User
from app.repositories.user_repository import UserRepository
from datetime import timedelta
import jwt

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def authenticate_user(self, db: AsyncSession, username: str, password: str) -> Optional[User]:
        user = await self.repository.get_by_username(db, username)
        if not user or not self.verify_password(password, user.hashed_password):
            return None
        return user

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        # Password verification logic
        return True  # Simplified for example

    def create_access_token(self, data: dict, expires_delta: timedelta = None) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, "SECRET_KEY", algorithm="HS256")
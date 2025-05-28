from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from app.models.user import User

class UserRepository:
    def __init__(self, model: User):
        self.model = model

    async def get_by_id(self, db: AsyncSession, id: int) -> Optional[User]:
        result = await db.execute(select(self.model).where(self.model.id == id))
        return result.scalars().first()

    async def get_by_username(self, db: AsyncSession, username: str) -> Optional[User]:
        result = await db.execute(select(self.model).where(self.model.username == username))
        return result.scalars().first()

    async def list(self, db: AsyncSession, skip: int = 0, limit: int = 100) -> List[User]:
        result = await db.execute(select(self.model).offset(skip).limit(limit))
        return result.scalars().all()
from fastapi import APIRouter, Depends
from app.schemas.user import UserSchema
from app.services.user_service import UserService
from app.db.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get("/users/me", response_model=UserSchema)
async def read_users_me(current_user: UserSchema = Depends(UserService.get_current_user)):
    return current_user

@router.get("/admin/users/", response_model=List[UserSchema])
@requires_role("admin")
async def list_users(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db),
    current_user: UserSchema = Depends(UserService.get_current_user)
):
    user_service = UserService()
    users = await user_service.list_users(db, skip=skip, limit=limit)
    return users
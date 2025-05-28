from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.dependencies import get_db
from app.schemas.user import UserSchema
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository

router = APIRouter()

@router.post("/token")
async def login(username: str, password: str, db: AsyncSession = Depends(get_db)):
    user_repo = UserRepository()
    user_service = UserService(user_repo)
    user = await user_service.authenticate_user(db, username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = user_service.create_access_token(
        data={"sub": user.username}, expires_delta=timedelta(minutes=30)
    )
    return {"access_token": access_token, "token_type": "bearer"}
from fastapi import APIRouter

router = APIRouter()

from .endpoints import auth, users

router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(users.router, prefix="/users", tags=["users"])
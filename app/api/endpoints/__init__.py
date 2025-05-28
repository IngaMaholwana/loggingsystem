# File: /loggingsystem/loggingsystem/app/api/endpoints/__init__.py
from fastapi import APIRouter

router = APIRouter()

from .auth import login
from .users import read_users_me, list_users

router.add_api_route("/token", login, methods=["POST"])
router.add_api_route("/users/me", read_users_me, methods=["GET"])
router.add_api_route("/admin/users/", list_users, methods=["GET"])
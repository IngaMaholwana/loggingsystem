# filepath: /loggingsystem/loggingsystem/app/__init__.py
from fastapi import FastAPI
from .api import api_router
from .core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

app.include_router(api_router)
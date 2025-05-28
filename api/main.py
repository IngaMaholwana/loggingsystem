from fastapi import FastAPI
from app.lifespan import lifespan
from app.core.middleware import TimingMiddleware
from app.api import auth, users

app = FastAPI(lifespan=lifespan)

app.add_middleware(TimingMiddleware)

app.include_router(auth.router)
app.include_router(users.router)
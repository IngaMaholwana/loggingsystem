from fastapi import FastAPI
from app.api.endpoints import auth, users
from app.middlewares.timing_middleware import TimingMiddleware
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application startup")
    yield
    print("Application shutdown")

app = FastAPI(lifespan=lifespan)
app.add_middleware(TimingMiddleware)

app.include_router(auth.router)
app.include_router(users.router)
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app):
    print("Application startup")
    yield
    print("Application shutdown")
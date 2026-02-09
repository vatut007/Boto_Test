from contextlib import asynccontextmanager
from fastapi import FastAPI

from api.routers import main_router
from core.config import settings
from services.db_init import db_init


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_init()
    yield

app = FastAPI(title=settings.app_title,
              description=settings.description,
              lifespan=lifespan)

app.include_router(main_router)

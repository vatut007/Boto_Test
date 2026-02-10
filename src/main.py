from contextlib import asynccontextmanager
import logging
import sys
from fastapi import FastAPI

from api.routers import main_router
from core.config import settings
from services.db_init import db_init

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    db_init()
    yield

app = FastAPI(title=settings.app_title,
              description=settings.description,
              lifespan=lifespan)

app.include_router(main_router)

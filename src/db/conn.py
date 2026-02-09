import asyncio
import sqlite3
from contextlib import asynccontextmanager
from core.config import settings


@asynccontextmanager
async def get_db_session():
    loop = asyncio.get_event_loop()
    conn = await loop.run_in_executor(
        None,
        lambda: sqlite3.connect(settings.database_url)
    )
    try:
        yield conn
    finally:
        await loop.run_in_executor(None, conn.close)


async def get_db():
    async with get_db_session() as db:
        yield db

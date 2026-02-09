import sqlite3
from core.config import settings


def get_db_session():
    with sqlite3.connect(settings.database_url) as session:
        yield session

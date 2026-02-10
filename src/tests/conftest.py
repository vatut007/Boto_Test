import sqlite3
import tempfile
import pytest
from fastapi.testclient import TestClient

from api.routers import main_router as router
from db.conn import get_db_session


@pytest.fixture
def db_file():
    """Создаёт временный SQLite‑файл для тестов."""
    db = tempfile.NamedTemporaryFile(delete=False, suffix=".db")
    yield db.name
    db.close()


@pytest.fixture
def test_db(db_file):
    """Инициализирует соединение с тестовой БД."""
    conn = sqlite3.connect(db_file, check_same_thread=False)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS URLMap (
            id INTEGER PRIMARY KEY,
            short TEXT UNIQUE NOT NULL,
            original TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn


@pytest.fixture
def client(test_db):
    """Возвращает тестовый клиент FastAPI с подменой зависимости get_db_session."""
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)

    def override_get_db():
        return test_db

    app.dependency_overrides[get_db_session] = override_get_db
    return TestClient(app)

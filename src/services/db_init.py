import sqlite3
from core.config import settings


def db_init():
    conn = sqlite3.connect(settings.database_url)
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS URLMap (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        short TEXT NOT NULL UNIQUE,
        original TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    '''

    try:
        cursor.execute(create_table_query)
        conn.commit()
        print("Таблица 'links' успешно создана или уже существует.")

    except sqlite3.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")

    finally:
        conn.close()

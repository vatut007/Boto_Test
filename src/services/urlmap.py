from sqlite3 import Connection
import string
from datetime import datetime
from core.config import settings
from schemas.urlmap import UrlMapRead


class URLMap():
    def __init__(self, conn: Connection) -> None:
        self.conn = conn

    def get_shorten(self, short: str):
        cursor = self.conn.cursor()
        get_query = "SELECT original FROM URLMap WHERE short=?"
        cursor.execute(get_query, (short,))
        row = cursor.fetchone()
        return row[0] if row else None

    def create_shorten(self, original: str):
        cursor = self.conn.cursor()
        insert_query = "INSERT INTO URLMap (short, original) VALUES (?,?)"
        cursor.execute(insert_query, (original+str(datetime.now()), original,))
        new_id = cursor.lastrowid
        if new_id:
            short = self.encode_id(new_id)
            update_query = "UPDATE URLMap SET short = ? WHERE id = ?"
            cursor.execute(update_query, (short, new_id))
            print(f"Создана ссылка: {short} → {original} (id={new_id})")
            self.conn.commit()
            return UrlMapRead(short_link=f'{settings.base_domain}/{short}')

    def encode_id(self, num: int,
                  alphabet: str = string.ascii_letters + string.digits,
                  min_length: int = 6) -> str:
        if num == 0:
            char = alphabet[0]
            return char * min_length

        encoded = []
        base = len(alphabet)
        while num:
            encoded.append(alphabet[num % base])
            num //= base
        result = ''.join(reversed(encoded))
        if len(result) < min_length:
            padding = alphabet[0] * (min_length - len(result))
            result = padding + result
        return result

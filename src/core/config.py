from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Сервис сокращения ссылок'
    description: str = 'Это апи сервиса сокращения ссыллок'
    database_url: str = './fastapi.db'

    class Config:
        env_file = '.env'


settings = Settings()

from pydantic import BaseModel, Field, HttpUrl, field_validator, validator


class UrlMapCreate(BaseModel):
    url: HttpUrl = Field()
    
    # @field_validator('url')
    # @classmethod
    # def check_scheme(cls, v: HttpUrl) -> HttpUrl:
    #     """Проверяет, что URL начинается с http:// или https://"""
    #     if not str(v).startswith('http://') and not str(v).startswith('https://'):
    #         raise ValueError('URL должен начинаться с http:// или https://')
    #     return v


class UrlMapRead(BaseModel):
    short_link: str

from pydantic import BaseModel, Field


class UrlMapCreate(BaseModel):
    url: str = Field()


class UrlMapRead(BaseModel):
    short_link: str

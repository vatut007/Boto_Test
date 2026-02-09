from http import HTTPStatus
from sqlite3 import Connection
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse

from db.conn import get_db_session
from schemas.urlmap import UrlMapCreate, UrlMapRead
from services.urlmap import URLMap

router = APIRouter()


@router.post('/shorten', response_model=UrlMapRead)
def create_shorten(shorten: UrlMapCreate,
                   session: Connection = Depends(get_db_session),
                   ):
    urlMap = URLMap(session)
    urlMap = urlMap.create_shorten(shorten.url)
    return urlMap


@router.get('/{code}')
def redirect_short_url(code: str,
                       session: Connection = Depends(get_db_session)):
    urlMap = URLMap(session)
    (original_url) = urlMap.get_shorten(code)
    print(original_url)
    if not original_url:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Ссылка не найдена"
        )
    return RedirectResponse(
        url=original_url,
        status_code=HTTPStatus.MOVED_PERMANENTLY,
    )

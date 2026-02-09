from fastapi import APIRouter
from .endpoints import url_map_router

main_router = APIRouter()
main_router.include_router(url_map_router)

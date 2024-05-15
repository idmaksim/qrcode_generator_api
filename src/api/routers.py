from fastapi import APIRouter
from . import generator


main_api_router = APIRouter(
    prefix='/api'
)

routers = [
    generator.router
]

[main_api_router.include_router(router) for router in routers]
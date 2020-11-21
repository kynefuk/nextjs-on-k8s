from fastapi import APIRouter

from . import views


api_router = APIRouter()
api_router.include_router(views.router, prefix="/todos", tags=["todos"])
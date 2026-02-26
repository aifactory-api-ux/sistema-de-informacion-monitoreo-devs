from fastapi import APIRouter
from backend.app.api.v1.endpoints import auth

api_router = APIRouter()

api_router.include_router(auth.router, tags=["auth"])
# Additional routers can be included here

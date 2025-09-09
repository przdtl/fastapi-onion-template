from fastapi import APIRouter

api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router()
api_v1_router.include_router()

__all__ = ["api_v1_router"]

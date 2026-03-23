from fastapi import APIRouter
from app.api.v1.endpoints import health, items

# Core Version 1 API Router
api_router = APIRouter()

# Include individual endpoints
api_router.include_router(health.router, tags=["Health"], prefix="/api/v1")
api_router.include_router(items.router, tags=["Items"], prefix="/api/v1/items")

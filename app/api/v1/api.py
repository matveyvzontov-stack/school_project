from fastapi import APIRouter
from app.api.v1.endpoints import health, items, users, notes

# Core Version 1 API Router
api_router = APIRouter()

# Include individual endpoints
api_router.include_router(health.router, tags=["Health"], prefix="/api/v1")
api_router.include_router(users.router, tags=["Users"], prefix="/api/v1/users")
api_router.include_router(notes.router, tags=["Notes"], prefix="/api/v1/notes")
api_router.include_router(items.router, tags=["Items"], prefix="/api/v1/items")

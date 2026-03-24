from fastapi import FastAPI
from app.api.v1.api import api_router
from app.api.v1.endpoints import home
from app.core.config import settings
from app.database import Base, engine

# Create Database Tables on startup (SQLite initializer)
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

# 1. Include Root Router (Handles / and /favicon.ico) without any prefix
app.include_router(home.router)

# 2. Include API versioning components to handle standard requests
app.include_router(api_router)

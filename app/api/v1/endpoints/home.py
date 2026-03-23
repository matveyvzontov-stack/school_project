from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "hello, world", "info": "Welcome to the modular FastAPI template!"}

# Serve favicon from the static folder
@router.get("/favicon.ico", include_in_schema=False)
async def favicon():
    # Looks for favicon in static/ folder
    favicon_path = os.path.join("static", "favicon.png")
    if os.path.exists(favicon_path):
        return FileResponse(favicon_path)
    # fallback to root if not moved yet
    return FileResponse("favicon.png")

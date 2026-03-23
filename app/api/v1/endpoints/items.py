from fastapi import APIRouter, HTTPException
from app.schemas.item import ItemResponse


router = APIRouter()

# Mock database
items = [
    {"id": 1, "name": "Item One", "description": "This is item one"},
    {"id": 2, "name": "Item Two", "description": "This is item two"},
]

@router.get("/")
async def get_items():
    """Get all items from current version API."""
    return {"items": items}

@router.get("/{item_id}")
async def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

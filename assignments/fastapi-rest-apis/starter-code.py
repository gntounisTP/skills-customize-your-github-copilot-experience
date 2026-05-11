from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Inventory API")


class Item(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


items = [
    {"id": 1, "name": "Keyboard", "price": 49.99, "in_stock": True},
    {"id": 2, "name": "Mouse", "price": 24.99, "in_stock": True},
    {"id": 3, "name": "Monitor", "price": 199.99, "in_stock": False},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Inventory API"}


@app.get("/items")
def get_items():
    # TODO: Return the full list of items.
    return {"items": items}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    # TODO: Return the matching item or raise HTTPException(status_code=404).
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items")
def create_item(item: Item):
    # TODO: Prevent duplicate IDs and append the new item.
    return {"message": "Implement item creation", "item": item.model_dump()}


@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    # TODO: Replace the matching item or raise HTTPException(status_code=404).
    return {
        "message": "Implement item update",
        "item_id": item_id,
        "item": updated_item.model_dump(),
    }


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # TODO: Remove the matching item or raise HTTPException(status_code=404).
    return {"message": f"Implement deletion for item {item_id}"}


# Run locally with:
# uvicorn starter-code:app --reload
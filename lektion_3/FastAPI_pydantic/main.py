from fastapi import FastAPI
from typing import Union

app = FastAPI(title="My First API APP")

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/items/{item_id}") # localhost:8000/items/248
def get_item(item_id: int, color: Union[str, None] = None):
    return {"item_id": item_id, "color": color}
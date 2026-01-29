from fastapi import FastAPI, status
from typing import Union
import requests
from schema.fox import FoxSchema
from schema.user import UserSchema, UserSchemaResponse

userList: list[UserSchema] = [
    UserSchema(username="user1", password="password1", is_enabled=True),
    UserSchema(username="user2", password="password2", is_enabled=True),
    UserSchema(username="user3", password="password3", is_enabled=True)
]


app = FastAPI(title="My First API APP")

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/items/{item_id}") # localhost:8000/items/248
def get_item(item_id: int, color: Union[str, None] = None):
    return {"item_id": item_id, "color": color}

@app.get("/users", response_model=list[UserSchemaResponse])
def get_users() -> list[UserSchemaResponse]:
    return userList


@app.post("/users", 
    response_model=UserSchema, 
    status_code=status.HTTP_201_CREATED)
def post_user(user: UserSchema) -> UserSchema:
    userList.append(user)
    return user

@app.get("/fox", response_model=FoxSchema)
def get_fox():
    response = requests.get("https://randomfox.ca/floof/")
    result_json = response.json()
    
    fox = FoxSchema(**result_json)
    return fox


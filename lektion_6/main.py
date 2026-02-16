from fastapi import FastAPI, status
from psycopg3 import Connect
from psycopg3 import ConnectionPool
from psycopg3.type.json import Json

DATABASE_URL = "postgres://Panzword88@localhost:5432/postgres"
pool = ConnectionPool(DATABASE_URL)
app = FastAPI(title="lektion-6-test-schema")

@app.get("/")
def read_root():
    return {"Hello": "World"}



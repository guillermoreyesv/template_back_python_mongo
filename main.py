# main.py

from fastapi import FastAPI
from contextlib import asynccontextmanager
from config.db import MongoDBSingleton
from routers.users import _index as users
import os


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        yield
    finally:
        MongoDBSingleton().close_connection()

app = FastAPI(
    title="TITLE",
    description="Docs for TITLE",
    version="1.0",
    docs_url=os.getenv('DOCS_URL','/docs'), 
    redoc_url=os.getenv('REDOC_URL','/redoc'),
    lifespan=lifespan
)

version = "/v1"
app.include_router(users.router, prefix=version+"/users", tags=["users"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001, log_level="warning")

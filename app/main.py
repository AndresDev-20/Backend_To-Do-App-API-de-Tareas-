from fastapi import FastAPI
from app.core.config import settings
from app.db import base

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)


@app.get("/")
def read_root():
    return {"Hello": "World"}
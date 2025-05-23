from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings
from app.api.routes import user, task

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

oauth2_sheme = OAuth2PasswordBearer(tokenUrl="users/login")

app.include_router(user.router, prefix="/users", tags=["Etiquetas(users)"])
app.include_router(task.router, prefix="/tasks", tags=["Etiqueta(Tasks)"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
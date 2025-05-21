# Segundo paso: definir los esquemas de que cada endpoint para poder tranferir informacion
from pydantic import BaseModel
from app.schemas.task import TaskSchema

class UserSchema(BaseModel):
    name: str
    email: str
class User(UserSchema):
    id: int
    tasks: list[TaskSchema] = []

    class Config:
        from_attributes: True
class UserCreate(UserSchema):
    pass
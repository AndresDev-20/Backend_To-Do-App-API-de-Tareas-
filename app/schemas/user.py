# Segundo paso: definir los esquemas de que cada endpoint para poder tranferir informacion
from pydantic import BaseModel
from app.schemas.task import TaskSchema
from typing import List

class UserSchema(BaseModel):
    name: str
    email: str
class User(UserSchema):
    id: int
    tasks: List[TaskSchema] = []

    class Config:
        from_attributes: True
class UserCreate(UserSchema):
    password: str
    pass


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
# Segundo paso: definir los esquemas de que cada endpoint para poder tranferir informacion
from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    email: str
class User(UserSchema):
    id: int

    class Config:
        from_attributes: True
class UserCreate(UserSchema):
    pass
from pydantic import BaseModel

class TaskSchema(BaseModel):
    title: str
    user_id: int

class Task(TaskSchema):
    id: int

    class Config:
        from_attributes = True

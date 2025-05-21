from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskSchema


# Obtenemos las tareas
def get_task(db: Session):
    return db.query(Task).all()


# Obtener una tarea por id
def get_task_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


# Crear una tarea
def create_task(db: Session, data: TaskSchema):
    new_task = Task(title = data.title, user_id = data.user_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


# Actualizamos una tarea
def update_task(db: Session, task_id: int, data: TaskSchema):
    search_task = db.query(Task).filter(Task.id == task_id).first()
    if not search_task:
        return {"message": "Tarea no encontrada"}
    for field, value in data.dict().items():
        setattr(search_task, field, value)
    db.commit()
    db.refresh(search_task)
    return search_task


# Eliminar por id
def delete_task(db: Session, task_id: int):
    search_task = db.query(Task).filter(Task.id == task_id).first()
    db.delete(search_task)
    db.commit()
    return {"message": "La tarea ha sido eliminada"}

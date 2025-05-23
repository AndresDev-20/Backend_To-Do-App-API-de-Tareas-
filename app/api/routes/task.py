from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.crud import task as task_crud
from app.schemas import task as task_schema
from app.auth.deps import get_current_user

router = APIRouter()

@router.get("/", response_model=List[task_schema.TaskSchema])
async def read_task(db: Session = Depends(get_db),  current_user: task_schema.Task = Depends(get_current_user)):
    return task_crud.get_task(db)


@router.get("/{task_id}", response_model=task_schema.TaskSchema)
async def task_by_id(task_id: int, db: Session = Depends(get_db), current_user: task_schema.Task = Depends(get_current_user)):
    db_task = task_crud.get_task_id(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_task


@router.post("/create", response_model=task_schema.TaskSchema)
async def add_task(data: task_schema.TaskSchema, db: Session = Depends(get_db), current_user: task_schema.Task = Depends(get_current_user)):
    return task_crud.create_task(db=db, data=data)


@router.put("/update/{task_id}")
async def task_update(task_id: int, data: task_schema.TaskSchema, db: Session = Depends(get_db), current_user: task_schema.Task = Depends(get_current_user)):
    db_task = task_crud.get_task_id(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task_crud.update_task(db=db, task_id=task_id, data=data)


@router.delete("/delete/{task_id}")
async def task_delete(task_id: int, db:Session = Depends(get_db), current_user: task_schema.Task = Depends(get_current_user)):
    db_task = task_crud.get_task_id(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task_crud.delete_task(db=db, task_id=task_id)
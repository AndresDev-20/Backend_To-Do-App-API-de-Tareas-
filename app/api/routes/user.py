# Cuarto paso definir los endpoints de nuestro proyecto
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.crud import user as user_crud
from app.schemas import user as user_schema
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.jwt import create_access_token
from app.auth.deps import get_current_user
from app.core.config import settings
import datetime

router = APIRouter()

@router.get("/", response_model=List[user_schema.User])
async def read_user(db: Session = Depends(get_db), current_user: user_schema.User = Depends(get_current_user)):
    return user_crud.get_user(db)

@router.get("/{user_id}", response_model=user_schema.User)
async def read_user_id(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

@router.post("/create", response_model=user_schema.UserSchema)
async def create_user(user: user_schema.UserCreate, db:Session = Depends(get_db)):
    return user_crud.create_user(db=db, user=user)


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas"
        )
    access_token_expires = datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": str(user.id)}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@router.put("/update/{user_id}")
async def update_user(user_id: int, user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user_crud.update_user(db=db, user_id=user_id, user=user)

@router.delete("/delete/{user_id}", response_model=user_schema.User)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="usuario no existe")
    return user_crud.delete_user(db=db, user_id=user_id)
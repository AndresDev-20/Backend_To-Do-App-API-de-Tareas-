from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.crud import user as user_crud
from app.schemas.user import User
from app.core.config import settings  # Aquí defino SECRET_KEY y algoritmo

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")  # Revisa si usas "/login" u otra ruta

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Acceso denegado, inicia sesión",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = user_crud.get_user_id(db, user_id=int(user_id))
    if user is None:
        raise credentials_exception
    return user

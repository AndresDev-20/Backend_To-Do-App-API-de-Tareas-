#Tercer paso configurar el crud que esto actua como los controladores en un proyecto de node.js
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserSchema
from sqlalchemy.orm import joinedload
from app.core.security import hash_password
from app.core.security import verify_password


# Obtenemos toda la lista de los usuarios
def get_user(db: Session):
    return db.query(User).options(joinedload(User.tasks)).all()

# Obtenemos un usuario por su id
def get_user_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Creamos un usuario
def create_user(db: Session, user: UserSchema):
    # Segundo paso para bcrypt
    hashed_password = hash_password(user.password)
    db_user = User(name=user.name, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Login para logear a un usuario
def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user

# Actualizamos un usuario
def update_user(db: Session, user_id: int, user:UserSchema):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    db_user.name = user.name
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user

# Eliminamos un usuario
def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return db_user



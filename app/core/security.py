# Pirmer paso crar este archivo y configurarlo
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Encriptar contraseña
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Verificar contraseña
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

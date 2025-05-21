from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"
    id:int = Column(BigInteger, primary_key=True, index=True)
    name:str = Column(String)
    email:str = Column(String, unique=True, index=True)

    # Relacion
    tasks = relationship("Task", back_populates="users")
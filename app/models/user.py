from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class User(Base):
    id:int = Column(BigInteger, primary_key=True, index=True)
    name:str = Column(String)
    email:str = Column(String, unique=True, index=True)

    task = relationship("Taks", back_populates="user")
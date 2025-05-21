from sqlalchemy import Column, BigInteger, ForeignKey, String, Table
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Task(Base):
    __tablename__ = "tasks"
    id:int = Column(BigInteger, primary_key=True, index=True)
    title:str = Column(String, index=True)
    user_id = Column(BigInteger, ForeignKey('users.id'))

    # Relaciones
    users = relationship("User", back_populates="tasks")
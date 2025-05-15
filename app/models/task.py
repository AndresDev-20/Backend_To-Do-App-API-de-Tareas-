from sqlalchemy import Column, BigInteger, ForeignKey, String, Table
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Task(Base):
    id:int = Column(BigInteger, primary_key=True, index=True)
    title:str = Column(String, index=True)
    user_id = Column(BigInteger, ForeignKey('user.id'))

    # Relaciones
    user = relationship("User", back_populates="task")
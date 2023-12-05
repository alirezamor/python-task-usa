from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # Establishing a one-to-many relationship with tasks
    tasks = relationship("Task", back_populates="user")

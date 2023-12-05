import sys
from sqlalchemy import Column, String, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship

sys.path.append("..")
from src.database import Base


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(String, nullable=False)
    status = Column(String, nullable=False, index=True)
    custom_fields = Column(JSON)

    # Foreign key relationship with the User table
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    user = relationship("User", back_populates="tasks")

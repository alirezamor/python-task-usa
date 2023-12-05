from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class TaskBase(BaseModel):
    name: str
    description: str
    status: str
    custom_fields: Optional[dict]


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    id: int
    user: User

    class Config:
        from_attributes = True


class TaskResponse(TaskBase):
    id: int

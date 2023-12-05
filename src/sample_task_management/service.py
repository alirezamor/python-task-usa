from sqlalchemy.orm import Session
from sqlalchemy import cast, Text
from .models import Task
from .schemas import TaskCreate, TaskUpdate


def create_task(db: Session, task: TaskCreate, user_id: int):
    db_task = Task(**task.model_dump(), user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Task).offset(skip).limit(limit).all()


def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def update_task(db: Session, task_id: int, task_update: TaskUpdate):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        for field, value in task_update.model_dump(exclude_unset=True).items():
            setattr(db_task, field, value)
        db.commit()
        db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task


def search_on_tasks(name: str, status: str, custom_field_name: str, custom_field_value: str, db):
    """
        Search for tasks based on name, status, and custom field name.
    """
    query = db.query(Task)

    if name:
        query = query.filter(Task.name.ilike(f"%{name}%"))

    if status:
        query = query.filter(Task.status.ilike(f"%{status}%"))

    if custom_field_name and custom_field_value:
        query = query.filter(
            cast(Task.custom_fields[custom_field_name], Text).ilike(f"%{custom_field_value}%")
        )

    tasks = query.all()
    return tasks

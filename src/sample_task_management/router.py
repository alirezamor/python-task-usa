import sys
from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from .schemas import TaskResponse
from .service import *

sys.path.append("..")
from src.database import SessionLocal

router = APIRouter(
    prefix="/task",
    tags=["task"],
    responses={
        404: {"task": "Not Found"}
    }
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# API Endpoints
@router.post("/tasks/", response_model=TaskResponse)
async def create_task_api(task: TaskCreate, user_id: int, db: Session = Depends(get_db)):
    return create_task(db, task, user_id)


@router.get("/tasks/", response_model=List[TaskResponse])
async def read_tasks_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_tasks(db, skip=skip, limit=limit)


@router.get("/tasks/{task_id}", response_model=TaskResponse)
async def read_task_api(task_id: int, db: Session = Depends(get_db)):
    task = get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task_api(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    task = update_task(db, task_id, task_update)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/tasks/{task_id}", response_model=TaskResponse)
async def delete_task_api(task_id: int, db: Session = Depends(get_db)):
    task = delete_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.get("/tasks/search/", response_model=List[TaskResponse])
async def search_tasks(
        name: str = Query(None, title="Search by task name"),
        status: str = Query(None, title="Search by task status"),
        custom_field_name: str = Query(None, title="Search by custom field name"),
        custom_field_value: str = Query(None, title="Search by custom field value"),
        db: Session = Depends(get_db)
):

    tasks = search_on_tasks(name, status, custom_field_name, custom_field_value, db)
    return tasks

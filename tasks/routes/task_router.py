from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from tasks.schemas.task import TaskCreate, Task
from tasks.services.task_service import get_tasks, create_task, delete_task_by_id
from core.database import get_db

tasks_router = APIRouter(prefix="/tasks", tags=["Tasks"])

@tasks_router.get("/", response_model=list[Task])
def read_tasks(db: Session = Depends(get_db)):
    return get_tasks(db)

@tasks_router.post("/", response_model=Task)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)

@tasks_router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    delete_task_by_id(db, task_id)
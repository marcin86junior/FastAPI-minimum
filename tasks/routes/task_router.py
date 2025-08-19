from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from tasks.schemas.task import TaskCreate, Task
from tasks.services.task_service import get_tasks, create_task
from core.database import get_db

tasks_router = APIRouter(prefix="/tasks", tags=["Tasks"])

@tasks_router.get("/", response_model=list[Task])
def read_tasks(db: Session = Depends(get_db)):
    return get_tasks(db)

@tasks_router.post("/", response_model=Task)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    print('aaaaaaaaaaaaaaaaaaaaaaa')
    print('aaaaaaaaaaaaaaaaaaaaaaa')
    return create_task(db, task)

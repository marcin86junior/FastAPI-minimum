from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from tasks.schemas.task import TaskCreate, Task
from tasks.services.task_service import get_tasks, create_task, update_task, delete_task
from core.database import get_db
from auth.services.auth_service import get_current_user

tasks_router = APIRouter(prefix="/tasks", tags=["Tasks"])

@tasks_router.get("/", response_model=list[Task])
def read_tasks(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return get_tasks(db, current_user["id"])

@tasks_router.post("/", response_model=Task)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return create_task(db, task, current_user["id"])

@tasks_router.put("/{task_id}", response_model=Task)
def update_existing_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return update_task(db, task_id, task, current_user["id"])

@tasks_router.delete("/{task_id}")
def delete_existing_task(task_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    delete_task(db, task_id, current_user["id"])
    return {"message": "Task deleted"}
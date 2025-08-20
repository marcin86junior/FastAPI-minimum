from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from tasks.schemas.task import TaskCreate, Task
from tasks.services.task_service import get_tasks, create_task, delete_task_by_id
from core.database import get_db
from auth.services.auth_service import get_current_active_user
from user.models.user import User
from tasks.schemas.task import TaskResponse
from typing import List

tasks_router = APIRouter(prefix="/tasks", tags=["Tasks"])

@tasks_router.get("/", response_model=List[TaskResponse])
def read_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return get_tasks(db, current_user.id)

@tasks_router.post("/", response_model=Task)
def create_new_task(
        task: TaskCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
):
    return create_task(db, task, current_user.id)

@tasks_router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    delete_task_by_id(db, task_id)

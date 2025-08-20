from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from tasks.models.task import Task
from tasks.schemas.task import TaskCreate

def get_tasks(db: Session):
    return db.query(Task).all()

def create_task(db: Session, task: TaskCreate):
    db_task = Task(
        title=task.title,
        description=task.description,
        owner_id=1
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task_by_id(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
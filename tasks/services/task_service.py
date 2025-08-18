from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from tasks.models.task import Task
from tasks.schemas.task import TaskCreate


def get_tasks(db: Session, owner_id: int):
    return db.query(Task).filter(Task.owner_id == owner_id).all()


def create_task(db: Session, task: TaskCreate, owner_id: int):
    db_task = Task(
        title=task.title,
        description=task.description,
        owner_id=owner_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: Session, task_id: int, task: TaskCreate, owner_id: int):
    db_task = db.query(Task).filter(Task.id == task_id, Task.owner_id == owner_id).first()
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    db_task.title = task.title
    db_task.description = task.description
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int, owner_id: int):
    db_task = db.query(Task).filter(Task.id == task_id, Task.owner_id == owner_id).first()
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    db.delete(db_task)
    db.commit()
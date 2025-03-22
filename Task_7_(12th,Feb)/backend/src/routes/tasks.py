from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from src.services import schemas, crud
from src.config.database import get_db
from src.models import models

router = APIRouter()

# ✅ Update the schema to include `user_id` in the request body
class TaskCreateRequest(schemas.TaskCreate):
    user_id: int  # Ensure user_id is included in the body

@router.post("/tasks/", response_model=schemas.TaskOut)
def create_task(task_request: TaskCreateRequest, db: Session = Depends(get_db)):
    return crud.create_task(db, task_request, task_request.user_id)

@router.get("/tasks/", response_model=list[schemas.TaskOut])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()
@router.put("/tasks/{task_id}/", response_model=schemas.TaskOut)
def update_task(task_id: int, task_update: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db_task.title = task_update.title
    db_task.description = task_update.description
    db.commit()
    db.refresh(db_task)
    
    return db_task

@router.delete("/tasks/{task_id}/", response_model=dict)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(db_task)
    db.commit()

    return {"message": "Task deleted successfully"}


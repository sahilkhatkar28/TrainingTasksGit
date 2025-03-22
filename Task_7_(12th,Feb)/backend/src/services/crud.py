from sqlalchemy.orm import Session
from src.models import models
from src.services import schemas
from src.config.auth import get_password_hash

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_task(db: Session, task: schemas.TaskCreate, user_id: int):
    db_task = models.Task(title=task.title,
        description=task.description,
        completed=False,
        user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

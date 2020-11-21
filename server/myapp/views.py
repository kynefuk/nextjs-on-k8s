from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from . import models, schemas
from .deps import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.Todo])
def get_todos(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()


@router.post("/", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreateType, db: Session = Depends(get_db)):
    data = models.Todo(title=todo.title, done=todo.done)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


@router.put("/{id}", response_model=schemas.Todo)
def update_todo(id: int, todo: schemas.TodoUpdateType, db: Session = Depends(get_db)):
    updated_todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    updated_todo.update(todo.dict())
    db.commit()
    return updated_todo

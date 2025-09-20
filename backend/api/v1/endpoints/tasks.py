from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api import deps
from backend.api.deps import get_db, get_current_user
from backend.models.user import User
from backend.models.task import Task as TaskModel
from backend.schemas.task import Task as TaskSchema, TaskCreate, TaskUpdate
from backend.crud import task as task_crud

router = APIRouter()

# List all tasks for the current logged-in user
@router.get("/", response_model=List[TaskSchema])
def list_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> List[TaskModel]:
    return db.query(TaskModel).filter(TaskModel.user_id == current_user.id).all()

# Create a new medicine reminder
@router.post("/", response_model=TaskSchema)
def create_task(
    task_in: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(deps.get_current_user)):
    return task_crud.create(db, obj_in=task_in, user_id=current_user.id)

# Update an existing task (only if it belongs to current user)
@router.put("/{task_id}", response_model=TaskSchema)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> TaskModel:
    db_obj = task_crud.get(db, id=task_id)
    if not db_obj or db_obj.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_crud.update(db, db_obj=db_obj, obj_in=task_update.dict(exclude_unset=True))

# Delete a task (only if it belongs to current user)
@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> dict:
    db_obj = task_crud.get(db, id=task_id)
    if not db_obj or db_obj.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    task_crud.remove(db, id=task_id)
    return {"ok": True}

@router.get("/{task_id}", response_model=TaskSchema)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    return task

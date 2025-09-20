from sqlalchemy.orm import Session
from backend.crud.base import CRUDBase
from backend.models.task import Task as TaskModel
from backend.schemas.task import TaskCreate, TaskUpdate


class CRUDTask(CRUDBase[TaskModel, TaskCreate, TaskUpdate]):
    # Override create to associate a task with the current user
    def create_with_user(self, db: Session, *, obj_in: TaskCreate, user_id: int) -> TaskModel:
        db_task = TaskModel(**obj_in.dict(), user_id=user_id)
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task

    # Optionally, add a query for all tasks by a user
    def get_multi_by_user(self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100):
        return (
            db.query(TaskModel)
            .filter(TaskModel.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def update_task(db: Session, db_task: TaskModel, task_update: TaskUpdate):
        for field, value in task_update.dict(exclude_unset=True).items():
            setattr(db_task, field, value)
        db.commit()
        db.refresh(db_task)
        return db_task


task = CRUDTask(TaskModel)

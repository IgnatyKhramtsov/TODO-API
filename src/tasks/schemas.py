from datetime import datetime

from pydantic import BaseModel

from tasks.models import Status


class TaskCreate(BaseModel):
    task: str
    status: Status = Status.planned
    priority_id: int = 2


class TaskBase(TaskCreate):
    id: int
    created_at: datetime
    updated_at: datetime


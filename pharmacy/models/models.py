from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field


class TaskType(str, Enum):
    TYPE_A = "TYPE_A"
    TYPE_B = "TYPE_B"
    TYPE_C = "TYPE_C"


class TaskCreateRequest(BaseModel):
    type: TaskType
    payload: str = Field(..., min_length=100, max_length=200)
    tokens: int = Field(..., ge=10, le=50)


class Task(TaskCreateRequest):
    id: str
    created_at: datetime
    attempts: int = 0


class TaskQueue(BaseModel):
    tasks: list[Task]

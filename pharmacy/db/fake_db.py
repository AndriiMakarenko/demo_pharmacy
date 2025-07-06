from datetime import datetime
from typing import Optional
from pharmacy.models.models import Task, TaskCreateRequest, TaskQueue
from pharmacy.db.task_queue import TaskQueueManager
import uuid


class FakeDB:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if getattr(self, "_initialized", False):
            return
        self._initialized = True
        self.task_queue = TaskQueueManager(TaskQueue())

    def add_task(self, task_rq: TaskCreateRequest) -> Task:
        task = Task(
            id=str(uuid.uuid4()),
            type=task_rq.type,
            payload=task_rq.payload,
            tokens=task_rq.tokens,
            created_at=datetime.now(),
            attempts=0,
        )
        self.task_queue.enqueue(task)
        return task

    def get_next_task(self) -> Optional[Task]:
        return self.task_queue.dequeue()

    def update_task(self, task_id: str, status: str) -> bool:
        for task in self.task_queue:
            if task.id == task_id:
                if status == "completed":
                    self.task_queue.remove(task_id)
                elif status == "failed":
                    task.attempts += 1
                    if task.attempts >= self.task_queue.MAX_ATTEMPTS:
                        self.task_queue.remove(task_id)
                    else:
                        self.task_queue.requeue(task)
                return True
        return False

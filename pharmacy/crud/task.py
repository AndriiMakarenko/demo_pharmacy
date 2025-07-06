from pharmacy.db.fake_db import FakeDB
from pharmacy.models.models import TaskCreateRequest, Task


def create_task(task_rq: TaskCreateRequest) -> Task:
    task = FakeDB().task_queue.enqueue(Task(**task_rq.dict(), attempts=0))
    return task


def get_next_task() -> Task | None:
    return FakeDB().task_queue.dequeue()


def update_task_status(task_id: str, status: str) -> bool:
    tasks = FakeDB().task_queue._task_queue.tasks
    for task in tasks:
        if task.id == task_id:
            task.status = status
            if status == "failed":
                task.attempts += 1
                if task.attempts < FakeDB().task_queue.MAX_ATTEMPTS:
                    FakeDB().task_queue.requeue(task)
                else:
                    FakeDB().task_queue.remove(task_id)
            elif status == "completed":
                FakeDB().task_queue.remove(task_id)
            return True
    return False

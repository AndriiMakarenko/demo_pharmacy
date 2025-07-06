from pharmacy.models.models import Task, TaskQueue

class TaskQueueManager:
    MAX_ATTEMPTS = 3

    def __init__(self, task_queue: TaskQueue):
        self._task_queue = task_queue

    def enqueue(self, task: Task):
        self._task_queue.tasks.append(task)

    def requeue(self, task: Task):
        self._task_queue.tasks.append(task)

    def dequeue(self):
        while self._task_queue.tasks:
            task = self._task_queue.tasks.pop(0)
            if task.attempts < self.MAX_ATTEMPTS:
                return task
        return None

    def remove(self, task_id: str):
        self._task_queue.tasks = [t for t in self._task_queue.tasks if t.id != task_id]

    def __iter__(self):
        return iter(self._task_queue.tasks)

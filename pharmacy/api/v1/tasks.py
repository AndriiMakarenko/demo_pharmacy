from fastapi import APIRouter, HTTPException, Request, status, Depends
from pharmacy.models.models import TaskCreateRequest, Task
from pharmacy.core.auth import verify_auth
from pharmacy.crud.task import create_task, get_next_task, update_task_status

router = APIRouter()


@router.post("/new_task", response_model=Task, status_code=status.HTTP_201_CREATED)
async def post_new_task(
    task: TaskCreateRequest,
    _: None = Depends(verify_auth),
):
    return create_task(task)


@router.get("/next_task", response_model=Task, status_code=status.HTTP_200_OK)
async def get_task(_: None = Depends(verify_auth)):
    task = get_next_task()
    if task is None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    return task


@router.post("/update_task/{task_id}", status_code=status.HTTP_200_OK)
async def update_task(task_id: str, status_update: dict, _: None = Depends(verify_auth)):
    success = update_task_status(task_id, status_update.get("status"))
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"ok": True}

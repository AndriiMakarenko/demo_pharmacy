from fastapi import FastAPI

from pharmacy.api.v1.tasks import router as tasks_router
from pharmacy.core.config import Config

Config()
app = FastAPI()

app.include_router(tasks_router, tags=["Tasks"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("pharmacy.main:app", host="0.0.0.0", port=Config().port, reload=True)
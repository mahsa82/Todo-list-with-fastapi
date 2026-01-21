from fastapi import FastAPI
from contextlib import asynccontextmanager
from tasks.routes import router as tasks_routes



tags_metadata = [
    {
        "name": "tasks",
        "description": "Operation related to task management",
        "externalDocs":{
            "description":"More about tasks",
            "url":"https://example.com/docs/tasks"
        }
    }
]


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Application startapp")
    yield
    print("Application shutdown")
    
app = FastAPI(lifespan=lifespan)

app.include_router(tasks_routes)
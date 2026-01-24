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
    
app = FastAPI(
    title="Todo Application",
    description="This is a section for description",
    summary="This is a section for summery ",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Mahsa Alizade",
        "url": "http://x-force.example.com/contact/",
        "email": "mahsa.alizade8271@gmail.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    lifespan=lifespan,
    openapi_tags=tags_metadata
            )

app.include_router(tasks_routes,prefix="/api/v1")
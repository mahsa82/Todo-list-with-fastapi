from fastapi import APIRouter,Path,Depends,HTTPException,Query
from fastapi.responses import JSONResponse
from tasks.schemas import *
from tasks.models import TaskModel
from sqlalchemy.orm import Session
from core.database import get_db
from typing import List


router = APIRouter(tags=["tasks"],prefix="/todo")


@router.get("/tasks",response_model=List[TaskResponseSchema])
async def retrieve_tasks_list(
    # filtering
    completed: bool = Query(None, description="filter tasks based on being completed or not"),
    # limiting
    limit: int = Query(10,gt=0,le=50,description="limiting the number of items to retrieve"),
    # getting the other one
    offset: int = Query(0,gt=0,description="use for paginating base on passed items"),
    db:Session = Depends(get_db)):
    query = db.query(TaskModel)
    if completed is not None :
        query = query.filter_by(is_competed=completed)
        
    # one model for paginations    
    # {
    #     page:
    #     total_page:
    #     next_page:
    #     prev_page:
    #     result:[
            
    #     ]
    # }
    
    return query.limit(limit).all()

@router.get("/tasks/{task_id}",response_model=TaskResponseSchema)
async def retrieve_tasks_detail(task_id:int = Path(...,gt=0),db:Session = Depends(get_db)):
    task_obj = db.query(TaskModel).filter_by(id=task_id).first()
    if not task_obj:
        raise HTTPException(status_code=404,detail="Task not found")
    return task_obj

@router.post("/tasks",response_model=TaskResponseSchema)
async def create_task(request:TaskBaseSchema,db:Session = Depends(get_db)):
    task_obj = TaskModel(**request.model_dump())
    db.add(task_obj)
    db.commit()
    db.refresh(task_obj)
    return task_obj

@router.put("/tasks/{task_id}",response_model=TaskResponseSchema)
async def update_task(request:TaskUpdateSchema,task_id:int = Path(...,gt=0),db:Session = Depends(get_db)):
    task_obj = db.query(TaskModel).filter_by(id=task_id).first()
    if not task_obj:
        raise HTTPException(status_code=404,detail="Task not found")
    for field,value in request.model_dump(exclude_unset=True).items():
        setattr(task_obj, field, value)
        
    db.commit()
    db.refresh(task_obj)
    
    return task_obj

@router.delete("/tasks/{task_id}",status_code=204)
async def delete_task(task_id:int = Path(...,gt=0),db:Session = Depends(get_db)):
    task_obj = db.query(TaskModel).filter_by(id=task_id).first()
    if not task_obj:
        raise HTTPException(status_code=404,detail="Task not found")
    db.delete(task_obj)
    db.commit()


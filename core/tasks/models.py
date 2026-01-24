from sqlalchemy import Column,String,Text,Boolean,Integer,DateTime,func
from core.database import Base


class TaskModel(Base):
    __tablename__="tasks"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(150),nullable=False)
    description = Column(Text(500),nullable=True)
    is_completed = Column(Boolean,default=False)
    created_date = Column(DateTime,server_default=func.now())
    updated_date = Column(DateTime,server_default=func.now(),server_onupdate=func.now())
    
    def __repr__(self) -> str:
        return f"Task(id={self.id!r}, title={self.title!r}, is_done={self.is_done!r})"
    
from typing import Optional
from pydantic import BaseModel


class TodoBaseType(BaseModel):
    pass


class TodoCreateType(TodoBaseType):
    title: str
    done: bool = False


class TodoUpdateType(TodoBaseType):
    title: Optional[str]
    done: Optional[bool]


class Todo(TodoBaseType):
    id: int
    title: str
    done: bool

    class Config:
        orm_mode = True

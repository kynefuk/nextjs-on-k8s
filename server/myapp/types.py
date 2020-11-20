from pydantic import BaseModel


class TodoBaseType(BaseModel):
    id: int


class TodoCreateType(TodoBaseType):
    title: str
    done: bool = False


class Todo(TodoBaseType):
    title: str
    done: bool

    class Config:
        orm_mode = True

import sqlalchemy
from databases import Database
from pydantic import BaseModel

DB_URL = "sqlite:///example.db"
database = Database(DB_URL)

metadata = sqlalchemy.MetaData()

todos = sqlalchemy.Table(
    "todos",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("done", sqlalchemy.Boolean),
)

engine = sqlalchemy.create_engine(DB_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)


class Todo(BaseModel):
    id: int
    title: str
    done: bool

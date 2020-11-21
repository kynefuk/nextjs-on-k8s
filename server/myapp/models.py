from typing import Dict
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///../sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True, index=True
    )
    title = sqlalchemy.Column(sqlalchemy.String)
    done = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

    def update(self, dict: Dict):
        for k, v in dict.items():
            if k in self.__dict__:
                setattr(self, k, v)

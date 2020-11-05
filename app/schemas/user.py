# from datetime import datetime
from typing import List
from pydantic import BaseModel
from uuid import UUID
from .book import Book


class User(BaseModel):
    uuid: UUID
    username: str
    # created_at: datetime
    # updated_at: datetime

    class Config:
        orm_mode = True


class UserDetail(User):
    books: List[Book] = []

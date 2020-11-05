from pydantic import BaseModel
from uuid import UUID


class Book(BaseModel):
    uuid: UUID
    title: str

    class Config:
        orm_mode = True

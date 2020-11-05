import cruds.user as crud
from database import get_db
from fastapi import APIRouter, Depends
from schemas.user import \
    User as UserSchema, UserDetail as UserDetailSchema
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

router = APIRouter()


@router.get('/', response_model=List[UserSchema])
async def read_users(db: Session = Depends(get_db)):
    return crud.read_users(db=db)


@router.get('/{user_id}', response_model=UserDetailSchema)
async def read_user(user_id: UUID, db: Session = Depends(get_db)):
    return crud.read_user(user_id=user_id, db=db)

from fastapi import HTTPException
from models import User
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND
from uuid import UUID


def read_users(db: Session):
    items = db.query(User).all()
    return items


def read_user(db: Session, user_id: UUID):
    try:
        item = db.query(User).get(user_id)
    except BaseException:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')

    return item

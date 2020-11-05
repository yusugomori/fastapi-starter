from database import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin


class Book(Base, TimestampMixin):
    __tablename__ = 'books'

    uuid = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    title = Column(String(256), nullable=False)

    user_id = Column(
        UUIDType(binary=False),
        ForeignKey('users.uuid'),
        nullable=True
    )
    user = relationship(
        'User',
        back_populates='books'
    )

from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp


class TimestampMixin(object):
    created_at = Column(Timestamp, nullable=False,
                        server_default=text('current_timestamp'))
    updated_at = Column(Timestamp, nullable=False,
                        server_default=text('current_timestamp on update current_timestamp'))

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import DateTime
from database import Base


class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        nullable=False
    )

    check_in = Column(
        DateTime,
        nullable=True
    )

    check_out = Column(
        DateTime,
        nullable=True
    )

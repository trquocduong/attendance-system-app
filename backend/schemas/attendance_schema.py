from pydantic import BaseModel


class AttendanceCreate(BaseModel):

    user_id: int

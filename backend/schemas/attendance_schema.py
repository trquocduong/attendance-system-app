from pydantic import BaseModel


class AttendanceCreate(BaseModel):

    user_id: int


class CheckOutRequest(BaseModel):

    user_id: int


class AttendanceUpdate(BaseModel):
    user_id: int

from fastapi import APIRouter

from database import SessionLocal

from schemas.attendance_schema import AttendanceCreate

from services.attendance_service import (
    check_in_service
)

router = APIRouter()


@router.post("/check-in")
def check_in(data: AttendanceCreate):

    db = SessionLocal()

    result = check_in_service(
        db,
        data.user_id
    )

    db.close()

    return {
        "message": "Check In Success",
        "attendance_id": result.id
    }

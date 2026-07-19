from fastapi import APIRouter

from database import SessionLocal

from schemas.attendance_schema import AttendanceCreate, CheckOutRequest

from services.attendance_service import (
    check_in_service,
    check_out_service,
    get_attendance_history,
    del_attendance

)

router = APIRouter()


@router.get("/attendance")
def get_attendance():
    db = SessionLocal()

    attendance = get_attendance_history(db)

    db.close()

    return attendance


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


@router.post("/checkout")
def checkout(data: CheckOutRequest):

    db = SessionLocal()

    result = check_out_service(
        db,
        data.user_id
    )

    db.close()

    if not result:
        return {
            "message": "Attendance not found"
        }

    return {
        "message": "Check Out Success",
        "attendance_id": result.id,
        "check_out": result.check_out
    }
    
@router.delete("/attendance/{user_id}")
def delete_attendance(user_id:int):
    db = SessionLocal()
    result = del_attendance(db, user_id)
    db.close()
    return {
        "message": "User delete",
        "data": result.id
    }

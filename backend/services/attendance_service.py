from datetime import datetime

from models.attendance_model import Attendance


def get_attendance_history(db):
    attendance = db.query(Attendance).all()
    return attendance


def check_in_service(db, user_id):
    attendance = Attendance(
        user_id=user_id,
        check_in=datetime.now()

    )
    db.add(attendance)
    db.commit()
    db.refresh(attendance)
    return attendance


def check_out_service(
        db,
        user_id
):

    attendance = (
        db.query(Attendance)
        .filter(
            Attendance.user_id == user_id,
            Attendance.check_out == None
        )
        .order_by(
            Attendance.id.desc()
        )
        .first()
    )

    if not attendance:
        return None

    attendance.check_out = datetime.now()

    db.commit()

    db.refresh(attendance)

    return attendance
def del_attendance(db,user_id):
    attendance = db.query(Attendance).filter(Attendance.id == user_id).first()
    if not attendance:
        db.close()
        return{
            "message":"Attendance Not found"
        }
    db.delete(attendance)
    db.commit()
    return attendance
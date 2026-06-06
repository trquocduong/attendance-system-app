from datetime import datetime

from models.attendance_model import Attendance


def check_in_service(db, user_id):
    attendance = Attendance(
        user_id=user_id,
        check_in=datetime.now()

    )
    db.add(attendance)
    db.commit()
    db.refresh(attendance)
    return attendance

from fastapi import FastAPI

from routers.user_router import router as user_router
from routers.attendance_router import router as attendance_router

from database import engine
from database import Base

from models.user_model import User
from models.attendance_model import Attendance


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)
app.include_router(attendance_router)

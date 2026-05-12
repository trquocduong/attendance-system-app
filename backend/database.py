from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql://attendance_user:attendance_password@localhost:55432/attendance_db"

engine = create_engine(DATABASE_URL)
# factory tạo session DB.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base = declarative_base()
# Đây là class gốc cho ORM.

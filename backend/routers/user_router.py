from fastapi import APIRouter
from database import SessionLocal
from schemas.user_schema import UserCreate, UserUpdate, UserLogin
from services.user_service import create_user_service, get_user_service, put_user_service, del_user_service, login_auth_service

router = APIRouter()


@router.get("/")
def home():
    return {"message ": "Start Attendace App"}
# get users


@router.get("/users")
def get_users():

    db = SessionLocal()

    users = get_user_service(db)

    db.close()

    return users


@router.post("/users")
def create_user(user: UserCreate):

    db = SessionLocal()

    result = create_user_service(db, user)

    db.close()

    return {
        "message": "User created",
        "data": result.id
    }


@router.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    db = SessionLocal()
    result = put_user_service(db, user, user_id)
    db.close()
    return {
        "message": "User update",
        "data": result.id
    }


@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    db = SessionLocal()
    result = del_user_service(db, user_id)
    db.close()
    return {
        "message": "User delete",
        "data": result.id
    }


@router.post("/login")
def login(user: UserLogin):
    db = SessionLocal()
    result = login_auth_service(
        db,
        user
    )
    db.close()
    if result is None:
        return {
            "message": "Email not found"
        }
    if result is False:
        return {
            "message": "Invalid password"
        }
    return {
        "message": "Login success",
        "data": {
            "id": result.id,
            "name": result.name,
            "email": result.email
        }
    }

from fastapi import FastAPI
from pydantic import BaseModel
from database import engine, SessionLocal
from models import User, Base
from schemas import UserUpdate, UserCreate

app = FastAPI()

# fake database user
# users = []


# Pydanti schema
# class UserCreate(BaseModel):
#     name : str
#     email:str
#     age:int
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message ": "Start Attendace App"}


# @app.get("/users")
# def hello():
#     return users


# @app.post("/users")
# def create_user(user: UserCreate):
#     users.append(user.dict())

#     return {
#         "message": "User created successfully",
#         "data": user
#     }

# get users

@app.get("/users")
def get_user():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users
# add users


@app.post("/users")
def create_user(user: UserCreate):
    db = SessionLocal()

    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()

    return {
        "message": "User created successfully",
        "data": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email
        }
    }


@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    db = SessionLocal()
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        db.close()
        return {
            "message": "User not found"
        }
    existing_user.name = user.name
    existing_user.email = user.email
    db.commit()
    db.refresh(existing_user)

    db.close()

    return {
        "message": "User updated successfully"
    }


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    db = SessionLocal()
    existing_user = db.query(User).filter(User.id == user_id).first()

    if not existing_user:
        db.close()

        return {
            "message": "User not found"
        }

    db.delete(existing_user)

    db.commit()

    db.close()

    return {
        "message": "User deleted successfully"
    }

from fastapi import FastAPI
from pydantic import BaseModel
from database import engine, SessionLocal
from models import User, Base


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

@app.post("/users")
def create_user():
    db = SessionLocal()

    new_users = User(
        name="I am Duong",
        email="duong@gmail.com",
        password="12345"
    )
    db.add(new_users)
    db.commit()
    db.close()

    return {"message": "user created"}

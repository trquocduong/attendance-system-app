from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# fake database user
users = []


# Pydanti schema
class UserCreate(BaseModel):
    name : str
    email:str
    age:int



@app.get("/")
def home():
    return { "message ": "Start Attendace App"}
@app.get("/users")
def hello():
    return users
@app.post("/users")
def create_user(user:UserCreate):
    users.append(user.dict())
    
    return {
        "message":"User created successfully",
        "data":user
    }
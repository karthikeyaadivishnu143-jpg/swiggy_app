from fastapi import APIRouter
from schemas import UserCreate

router=APIRouter(prefix="/users",tags=["Users"])

users=[]

@router.post("/")
def create_user(user:UserCreate):
    users.append(user.model_dump())
    return {"message":"User created","data":user}

@router.get("/")
def get_users():
    return users
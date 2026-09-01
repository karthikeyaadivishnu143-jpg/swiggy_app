from fastapi import APIRouter
from schemas import MenuCreate

router=APIRouter(prefix="/menu",tags=["Menu"])

menu=[]

@router.post("/")
def add_item(item:MenuCreate):
    menu.append(item.model_dump())
    return {"message":"Item added"}

@router.get("/")
def get_menu():
    return menu
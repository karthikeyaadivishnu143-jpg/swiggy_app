from fastapi import APIRouter
from schemas import RestaurantCreate

router=APIRouter(prefix="/restaurants",tags=["Restaurants"])

restaurants=[]

@router.post("/")
def add_restaurant(data:RestaurantCreate):
    restaurants.append(data.model_dump())
    return {"message":"Restaurant added"}

@router.get("/")
def list_restaurants():
    return restaurants
from pydantic import BaseModel

class UserCreate(BaseModel):
    name:str
    email:str

class RestaurantCreate(BaseModel):
    name:str
    cuisine:str

class MenuCreate(BaseModel):
    name:str
    price:float
    restaurant:str
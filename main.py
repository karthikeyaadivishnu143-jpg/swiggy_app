from fastapi import FastAPI
from database import Base,engine
from routers import users,restaurants,menu,cart,orders

Base.metadata.create_all(bind=engine)

app=FastAPI(title="FoodieGo API")

app.include_router(users.router)
app.include_router(restaurants.router)
app.include_router(menu.router)
app.include_router(cart.router)
app.include_router(orders.router)

@app.get("/")
def home():
    return {"message":"Welcome to FoodieGo"}
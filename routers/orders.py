from fastapi import APIRouter

router=APIRouter(prefix="/orders",tags=["Orders"])

orders=[]

@router.post("/place")
def place_order():
    orders.append("Order placed")
    return {"message":"Order placed successfully"}

@router.get("/")
def get_orders():
    return orders
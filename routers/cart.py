from fastapi import APIRouter

router=APIRouter(prefix="/cart",tags=["Cart"])

cart=[]

@router.post("/{item}")
def add_to_cart(item:str):
    cart.append(item)
    return {"message":"Added to cart"}

@router.get("/")
def view_cart():
    return cart
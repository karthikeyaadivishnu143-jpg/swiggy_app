from sqlalchemy import Column,Integer,String,Float
from database import Base

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)

class Restaurant(Base):
    __tablename__="restaurants"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    cuisine=Column(String)

class MenuItem(Base):
    __tablename__="menu_items"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    price=Column(Float)
    restaurant=Column(String)
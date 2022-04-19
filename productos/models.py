from tkinter import CASCADE
from sqlalchemy import column, Integer, String, float, text, ForeignKey
from sqlalchemy.orm import relationship
from eapp.database.session import base

class Category(base):
    _tablename_="category"
    id = column(integer, primary_key= True, autoincrement= True)
    name = column(String(55))
    product = relationship("product", back_populates= "category")
    
class product(base):
    _tablename_= "products"
    name = column(String(60))
    quantity=column(Integer)
    description = column(text)
    price = column(float)
    category_id =column(Integer, ForeignKey("category_id", ondelete=CASCADE))
    Category=relationship("Category", back_populates= "products")
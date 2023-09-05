from datetime import datetime
from sanic.exceptions import SanicException
from sqlalchemy.orm import sessionmaker
from sanic.log import logger
from sqlalchemy import Column, Integer, String, Float, DateTime,create_engine
from faunadb import query as q
from faunadb.client import FaunaClient
from users import Base

client = FaunaClient(secret="fnAFNAjjZsAAzcxXOiKy6hcr8WiJQ6j9-DtnTzpp")

Session = sessionmaker(bind=client)
session = Session()


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer,primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float,nullable=False)
    created_at = Column(DateTime,default=datetime.now())
    
    def __rpr__(self):
        return "{} {}".format(self.name,self.price)
    
    
product = Product(name = "vans",price=90.00)

print(product)
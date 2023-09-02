from datetime import datetime
from sanic.exceptions import SanicException
from sanic.log import logger
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True)
    username = Column(String(50),nullable=False,unique=True)
    email = Column(String(100),unique=True,nullable=False)
    password = Column(String(200),unique=True)
    create_at = Column(DateTime,default=datetime.now())
    
    def __repr__(self):
        return "{} with {}".format(self.username,self.email)

firstUser = User(username = "shawan",email ="brauashawan41@gmail.com",password ="12345678")

print(firstUser)
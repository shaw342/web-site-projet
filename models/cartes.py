from datetime import datetime
from sanic.exceptions import SanicException
from sanic.log import logger
from sqlalchemy import Column, Integer, String, Float, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from models.users import User,Base

class Carte(Base):
    __tablename__ = "carte"
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey("users.id"))

    def __rpr__(self):
        return "{} {}".format(self.id,self.user_id)
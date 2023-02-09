from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, String, Integer, event, Float, Boolean
from datetime import datetime

import util

Base = declarative_base()

class Inventory(Base):
    __tablename__ = 'Inventory_table'
    id = Column(Integer, primary_key=True)
    stock = Column(Integer)

    def __init__(self):
        self.id = None
        self.stock = None

@event.listens_for(Inventory, 'after_insert')
def PostPersist(mapper, connection, target):

    


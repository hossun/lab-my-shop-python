from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, String, Integer, event, Float, Boolean
from datetime import datetime

import util
from OrderPlaced import OrderPlaced
from OrderCancelled import OrderCancelled

Base = declarative_base()

class Order(Base):
    __tablename__ = 'Order_table'
    id = Column(Integer, primary_key=True)
    productId = Column(String(50))
    qty = Column(Integer)
    customerId = Column(String(50))
    amount = Column(Float)
    status = Column(String(50))
    address = Column(String(50))

    def __init__(self):
        self.id = None
        self.productId = None
        self.qty = None
        self.customerId = None
        self.amount = None
        self.status = None
        self.address = None

@event.listens_for(Order, 'after_insert')
def PostPersist(mapper, connection, target):
    event = OrderPlaced()
    event = util.AutoBinding(target, event)

    event.Publish()
    

    
@event.listens_for(Order, 'before_insert')
def PrePersist(mapper, connection, target):

    
@event.listens_for(Order, 'before_delete')
def PreRemove(mapper, connection, target):
    event = OrderCancelled()
    event = util.AutoBinding(target, event)

    event.Publish()
    

    


from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, String, Integer, event, Float, Boolean
from datetime import datetime

import util
from DeliveryStarted import DeliveryStarted

Base = declarative_base()

class Delivery(Base):
    __tablename__ = 'Delivery_table'
    id = Column(Integer, primary_key=True)
    address = Column(String(50))
    customerId = Column(String(50))
    quantity = Column(Integer)
    orderId = Column(Integer)

    def __init__(self):
        self.id = None
        self.address = None
        self.customerId = None
        self.quantity = None
        self.orderId = None

@event.listens_for(Delivery, 'after_insert')
def PostPersist(mapper, connection, target):
    event = DeliveryStarted()
    event = util.AutoBinding(target, event)

    event.Publish()
    

    


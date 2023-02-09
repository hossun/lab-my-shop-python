from AbstractEvent import AbstractEvent
import json
from datetime import datetime

class DeliveryStarted(AbstractEvent):
    id : int
    address : str
    customerId : str
    quantity : int
    
    def __init__(self):
        super().__init__()
        self.id = None
        self.address = None
        self.customerId = None
        self.quantity = None


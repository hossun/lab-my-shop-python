from AbstractEvent import AbstractEvent
import json
from datetime import datetime

class OrderCancelled(AbstractEvent):
    id : int
    productId : str
    qty : int
    customerId : str
    amount : int
    status : str
    address : str
    
    def __init__(self):
        super().__init__()
        self.id = None
        self.productId = None
        self.qty = None
        self.customerId = None
        self.amount = None
        self.status = None
        self.address = None


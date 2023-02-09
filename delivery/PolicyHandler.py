import util
import DeliveryDB
from Delivery import Delivery
deliveryrepository = DeliveryDB.repository


from OrderPlaced import OrderPlaced

def wheneverOrderPlaced_AddToDeliveryList(data):
    event = OrderPlaced()
    event = util.AutoBinding(data, event)
    
    delivery = Delivery()
    deliveryrepository.save(delivery)
    


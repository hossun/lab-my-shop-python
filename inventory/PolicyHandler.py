import util
import InventoryDB
from Inventory import Inventory
inventoryrepository = InventoryDB.repository


from OrderPlaced import OrderPlaced

def wheneverOrderPlaced_DecreaseStock(data):
    event = OrderPlaced()
    event = util.AutoBinding(data, event)
    
    inventory = Inventory()
    inventoryrepository.save(inventory)
    
from OrderCancelled import OrderCancelled

def wheneverOrderCancelled_IncreaseStock(data):
    event = OrderCancelled()
    event = util.AutoBinding(data, event)
    
    inventory = Inventory()
    inventoryrepository.save(inventory)
    


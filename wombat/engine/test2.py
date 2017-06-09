from wombat import engine

descr = "Gown with Long Sleeves and Deep V" 
brand = "For Love & Lemons" 
item_type = "dresses"
items = engine.main.get_top_n_similar_items(descr, brand, item_type, algorithm='l')

print(items)
from wombat.models import dbsession, Item
items = dbsession.query(Item).filter(
        Item.brand == brand, 
        Item.item_type == item_type).all()
print(items)

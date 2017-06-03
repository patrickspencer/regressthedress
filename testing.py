import pandas as pd
from sqlalchemy import exists
from stylelend.models import dbsession, engine
from stylelend.models.items import Item
from stylelend.models.rentalitems import RentalItem
from stylelend.models.rentals import Rental

# items = dbsession.query(Item) \
#               .filter(RentalItem.id == event_id).first()
items = dbsession.query(Item).all()
# items = engine.execute('SELECT * FROM rental_items LIMIT 10;').fetchall()
# print(items[0:10])
# df = pd.read_sql_query('SELECT * FROM "items"', con=engine)
# print(df.columns)
# items = dbsession.query(Rental).first()
items = engine.execute('SELECT DISTINCT item_type FROM items;').fetchall()
brands = engine.execute('SELECT DISTINCT brand FROM items LIMIT 10;').fetchall()
bags = engine.execute('SELECT DISTINCT brand FROM items WHERE LIMIT 10;').fetchall()
items = [item[0] for item in items]
brands = [brand[0] for brand in brands]
items = engine.execute('SELECT DISTINCT item_type FROM items;').fetchall()
versace_bags = engine.execute(
        "SELECT \
        item_price \
        brand \
        item_type \
        FROM rental_items \
        INNER JOIN items ON items.id = rental_items.item_id \
        WHERE item_type = 'dresses' AND brand='Tibi';"
        ).fetchall()
text = """SELECT item_price, brand, item_type, cost, sku, rent_per_week, items.created_at, year_purchased, rent_per_week
FROM rental_items
INNER JOIN items ON items.id = rental_items.item_id
WHERE item_type = 'dresses' AND brand='Tibi';"""
print(items)
print(brands)
# for item in items:
#     print(item.item_type)

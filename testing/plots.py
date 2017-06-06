import pandas as pd
from sqlalchemy import exists
from stylelend.models import dbsession, engine
from stylelend.models.items import Item
from stylelend.models.rentalitems import RentalItem
from stylelend.models.rentals import Rental
import matplotlib.pyplot as plt

# items = dbsession.query(Item) \
#               .filter(RentalItem.id == event_id).first()
# items = dbsession.query(Item).all()
# df = pd.read_sql_query('SELECT * FROM "items"', con=engine)
# print(df.columns)

def get_item_types():
    res = engine.execute('SELECT DISTINCT item_type FROM items;').fetchall()
    return [item[0] for item in res]

def get_brands():
    res = engine.execute('SELECT DISTINCT brand FROM items;').fetchall()
    return [brand[0] for brand in res]

def find_by_type_and_brand(item_type, brand):
    item_type = item_type.replace("'", "''")
    brand = brand.replace("'", "''")

    query = "SELECT I.id, I.brand, I.item_type, I.cost, I.sku, \
    I.rent_per_week, I.created_at, I.title, I.description, \
    I.year_purchased, I.rent_per_week, \
    R.rental_date, R.return_date, \
    RI.item_price, RI.refunded, RI.fit_return, \
    RI.created_at, \
    RI.updated_at \
    FROM items I \
    LEFT JOIN rental_items RI ON I.id = RI.item_id \
    LEFT JOIN rentals R ON R.id = RI.rental_id \
    WHERE item_type='{}' and brand='{}';".format(item_type, brand)
    return engine.execute(query).fetchall()

def find_by_item_type(item_type):
    item_type = item_type.replace("'", "''")
    query = "SELECT I.id, I.cost, \
    I.rent_per_week,\
    RI.item_price\
    FROM items I\
    LEFT JOIN rental_items RI ON I.id = RI.item_id \
    WHERE item_type='{}';".format(item_type)
    return engine.execute(query).fetchall()

# res = find_by_item_type("dresses")
query = "SELECT I.id, I.brand, I.item_type, I.cost, I.sku, \
    I.rent_per_week, I.created_at, I.title, I.description, \
    I.year_purchased, I.rent_per_week, \
    R.rental_date, R.return_date, \
    RI.item_price, RI.refunded, RI.fit_return, \
    RI.created_at, \
    RI.updated_at \
    FROM items I \
    LEFT JOIN rental_items RI ON I.id = RI.item_id \
    LEFT JOIN rentals R ON R.id = RI.rental_id;"
df = pd.read_sql_query(query, engine)
print(df.columns)

#
# plt.plot()

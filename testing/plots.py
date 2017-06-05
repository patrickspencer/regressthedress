import re
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
    columns = """item_price, brand, item_type, cost, I.sku,
    rent_per_week, I.created_at, I.title, I.description, 
    year_purchased, rent_per_week,
    rental_date, return_date"""

    query = "SELECT {} FROM rental_items RI \
    INNER JOIN items I ON I.id = RI.item_id \
    LEFT JOIN rentals R ON R.id = RI.rental_id \
    WHERE item_type = '{}' AND brand='{}';".format(columns, item_type, brand)
    return engine.execute(query).fetchall()

# items = dbsession.query(Item).filter(Item.id == RentalItem.rental_id).all()

# print("Items: {}".format(get_item_types()))
item_types = get_item_types()
brands = get_brands()
# print("item types: {}".format(item_types[0:10]))
# print("Brands: {}".format(brands[0:10]))

def write_brand_item_type_freq():
    """
    Find the frequency of item types and brands. For example there might be
    1 Gucci bag or 2 Versace dresses. Write these frequencies to a file.
    """
    f = open('output.txt', 'w')
    for item_type in item_types:
        for brand in brands:
            res = find_by_type_and_brand(item_type, brand)
            if len(res) > 1:
                s = "Item Type: {}; Brand: {}; count: {}".format(item_type, brand, len(res))
                f.write(s + "\n")
    f.close()

input_text = "Riller white dresses"
# find_word(re.escape(brand), input_string)
# word = 'iller'
# res = re.search('\\b' + search + '\\b', input_text, flags=re.IGNORECASE)
# try:
#     print(res.group(0))
# except AttributeError:
#     print("No match")

def find_word(search, text):
    res = re.search('(\\b' + search + '\\b)', text, flags=re.IGNORECASE)
    try:
        return res.groups(0)
    except AttributeError:
        return False

def find_brand(input_string):
    l = []
    for brand in brands:
        b = re.escape(brand)
        if find_word(re.escape(brand), input_string):
            l.append(find_word(b, input_text))
        return l

def find_item_type(input_string):
    l = []
    for item in item_types:
        i = re.escape(item)
        if find_word(i, input_string):
            l.append(find_word(i, input_text))
        return l

print(find_brand(input_text))
print(find_item_type(input_text))

print(item_types)

# m = re.search('(?<=abc)def', 'abcdef')
# print(m.group(0))

# plt.scatter()

# item_type = item_type.replace("'", "''")
# brand = brand.replace("'", "''")

# print(brands)
# print(find_by_type_and_brand("dresses", "Versace"))
# find_by_type_and_brand("dresses", "Versace")

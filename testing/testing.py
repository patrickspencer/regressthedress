import re
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from sqlalchemy import exists
import matplotlib.pyplot as plt
from wombat.models import dbsession, engine
from wombat.models import Item, RentalItem
from wombat.models import RentalItem, Rental

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
    """
    Look through each brand in the database and try to find it in the input_text
    """
    l = []
    for brand in brands:
        b = re.escape(brand)
        if find_word(re.escape(brand), input_string):
            l.append(find_word(b, input_text))
        return l

def find_item_type(input_string):
    """
    Look through each item_type in the database and try to find it in the input_text
    """
    l = []
    for item in item_types:
        i = re.escape(item)
        if find_word(i, input_string):
            l.append(find_word(i, input_text))
        return l

# item_type = item_type.replace("'", "''")
# brand = brand.replace("'", "''")

input_text = "Gown with Long Sleeves and Deep V"
choices = find_by_type_and_brand('dresses', 'Jill Jill Stuart')
items = dbsession.query(Item).filter(Item.item_type == 'dresses').all()

d = {}
for item in items[0:10]:
    token = fuzz.token_sort_ratio(input_text, item.title)
    if len(d) <= 5:
        d[item.id] = token
    if min(d.values()) < token:
        d[item.id] = token
        d.pop(min(d, key=d.get), None)

l = []
while len(d) > 0:
    l.append((max(d, key=d.get), max(d.values())))
    d.pop(max(d, key=d.get))

# for i in l:
#     print(dbsession.query(Item).filter(Item.id == i[0]).first())
# d = {1: 2, 3: 6, 5: 10}
# print(len(d))
# print(min(d, key=d.get))
# print(min(d.values()))
# if 5 in l:
#     print("yes")
# print(len(items))

item = dbsession.query(Item).filter(Item.id == 2564).first()
print(item.rental)
# print(items[0].rental.item_price)

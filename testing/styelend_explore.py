import numpy as np
import pandas as pd
from wombat.models import dbsession, engine
from wombat.models import Item, RentalItem, Rental
import matplotlib.pyplot as plt
import matplotlib
plt.style.use('ggplot')
matplotlib.rcParams['figure.figsize'] = (20, 16)
%matplotlib inline

# res = find_by_item_type("dresses")
query = "SELECT I.id, I.brand, I.item_type, I.cost, I.sku, \
    I.rent_per_week, I.created_at, I.title, I.description, \
    I.year_purchased, R.rental_date, R.return_date, \
    RI.item_price, RI.refunded, RI.fit_return \
    FROM items I \
    LEFT JOIN rental_items RI ON I.id = RI.item_id \
    LEFT JOIN rentals R ON R.id = RI.rental_id;"
df = pd.read_sql_query(query, engine)

brand_query = "SELECT item_type, count(item_type) FROM items GROUP BY item_type ORDER BY count(item_type) DESC;"
brand_df = pd.read_sql_query(brand_query, engine)
brand_df
brand_df.plot(kind='bar', x='item_type')

brand_query = "SELECT brand, count(brand) FROM items GROUP BY brand ORDER BY count(brand) DESC;"
brand_df = pd.read_sql_query(brand_query, engine)

def get_attr_by_brand_and_type(brand, item_type, attr):
    return df.loc[(df['brand'] == brand) & (df['item_type'] == item_type)][attr]

l = []
n = 20
for brand in brand_df['brand'][1:n]:
    rents = get_attr_by_brand_and_type(brand, 'dresses', 'rent_per_week')[df['rent_per_week'] < 10000].astype(int).values
    l.append((brand, rents))
data_arrays = [i[1] for i in l]
labels = [i[0] for i in l]

plt.boxplot(data_arrays, labels)
plt.xticks(list(range(1, n)), labels, rotation=80)
plt.show()

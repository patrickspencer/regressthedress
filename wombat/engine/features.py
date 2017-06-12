# -*- coding: utf-8 -*-
"""
    features
    ~~~~~~~~
    This modules is used for the following purposes
    1.) To create a point of reference for the creation of the predictive 
        model
    2.) To create a point of reference for the main parsing engine. Brand,
        item_type, and title are fed into the machine and from this we need to
        build a row in a database with the pertinent features. We need this
        file to keep track of what brands, item types, and adjectives from the
        title were used as features
"""

import pandas as pd
from wombat.models import dbsession, engine

# Make a list of most frequent brands of the form 'BCBG', 'BCBGMAXAZRIA','Alice + Olivia', etc...

# limit rent per week because some prices are set artificially high
rent_per_week_max = 1000

# Usually we just select all the brands but sometimes we need to limit the
# number we choose for testing purposes and it makes sense just to pick the
# most popular
top_brands_query = "SELECT brand, count(brand) FROM items WHERE brand != 'LENDER SUBMISSION FILL IN' GROUP BY brand ORDER BY count(brand) DESC;"
top_brand_df = pd.read_sql_query(top_brands_query, engine)
top_brands = ["\'{}\'".format(brand.replace("'", "''")) for brand in top_brand_df['brand']]
top_brands = ', '.join(top_brands)

query = "SELECT brand, item_type, cost, rent_per_week FROM items WHERE brand in ({}) AND rent_per_week < {}".format(top_brands, rent_per_week_max)
df = pd.read_sql_query(query, engine)

# get one-hot columns for brands 
dummified_brands = pd.get_dummies(df['brand'])
df = pd.concat([df, dummified_brands], axis = 1)
df = df.drop('brand', axis = 1)

# create the list of brands so other modules can access what brands are being
# used to create the model
brands = dummified_brands.columns.values

# get one-hot columns for item_types
dummified_items = pd.get_dummies(df['item_type'])
df = pd.concat([df, dummified_items], axis = 1)
df = df.drop('item_type', axis = 1)

# create the list of brands so other modules can access what brands are being
# used to create the model
item_types = dummified_items.columns.values

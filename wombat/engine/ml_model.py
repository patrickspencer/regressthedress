# -*- coding: utf-8 -*-
"""
    ml_model
    ~~~~~~~~
    Machine learning model file
    
    Holds dataframes and arrays that are used to make the machine learning
    model.

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
brands_query = "SELECT brand, count(brand) FROM items WHERE brand != 'LENDER SUBMISSION FILL IN' AND rent_per_week < {} GROUP BY brand ORDER BY count(brand) DESC;".format(rent_per_week_max)

brand_df = pd.read_sql_query(brands_query, engine)
brands_escaped = ["\'{}\'".format(brand.replace("'", "''")) for brand in brand_df['brand']]
brands_escaped = ', '.join(brands_escaped)

# create the list of brands so other modules can access what brands are being
# used to create the model
res = engine.execute(brands_query).fetchall()
brands = [r[0] for r in res]
brand_length = len(brands)

# grab items form db to train model.
# training query is the canonical query that the machine learning model is
# based on. If you change it then you have to reconstuct the model
canonical_query = "SELECT brand, item_type, title, cost, rent_per_week, description FROM items WHERE brand in ({}) AND rent_per_week < {}".format(brands_escaped, rent_per_week_max)
df = pd.read_sql_query(canonical_query, engine)
canonical_df = df

# get one-hot columns for brands 
dummified_brands = pd.get_dummies(df['brand'])
df = pd.concat([df, dummified_brands], axis = 1)
df = df.drop('brand', axis = 1)

# get one-hot columns for item_types
dummified_items = pd.get_dummies(df['item_type'])
df = pd.concat([df, dummified_items], axis = 1)
df = df.drop('item_type', axis = 1)

# create the list of brands so other modules can access what brands are being
# used to create the model
item_types = engine.execute('SELECT DISTINCT item_type FROM items;').fetchall()
item_types = [r[0] for r in item_types]

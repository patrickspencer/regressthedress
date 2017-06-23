# -*- coding: utf-8 -*-
"""
    predict_price
    ~~~~~~~~~~~~~
    The main module for parsing input clothing item into pandas dataframes that
    can be used to find the price using our model.

    The user inputs the following: 'brand', 'item_type', 'title'. We search the
    title for words in a predetermined list of words like 'chiffon', or 'lace'.
    These words were used in creating our model.
"""

import os
import re
import pandas as pd
import numpy as np
from wombat.engine import ml_model
from sklearn.externals import joblib
from wombat.models import dbsession, engine, ItemAdjective, ItemType

def create_one_hot_row_adj(sentence, features_adj):
    """Fuzzy search for words from ajective list in sentence"""
    l = []
    for feature in features_adj:
        match = re.search('{}'.format(feature), sentence, re.IGNORECASE)
        if match:
            l.append(1)
        else:
            l.append(0)
    return l

# used for brand and item_type
def create_one_hot_row(input_string, lexicon):
    l = []
    for phrase in lexicon:
        if input_string == lexicon:
            l.append(1)
        else:
            l.append(0)
    return l

# load model file
model_dir = '/home/patrick/Dropbox/insight/wombat/wombat/engine/stat_model_pickles'
model_dir = os.path.dirname(os.path.abspath(__file__))
model = os.path.join(model_dir, 'stat_model_pickles', 'rfr_v0.3_w_adj_prices_better_brands.pkl')
clf = joblib.load(model)

def create_one_hot_row_brand_keyword(unknown_brand, list_of_keywords):
    """Fuzzy search for words from list of keywords that describe a brand
    For example, if the unknown_brand = 'BCBGMAX' then this would match 'bcbg'
    and we would one-hot encode this against a list of brands
    """
    l = []
    counter = 0
    for keyword in list_of_keywords:
        match = re.search('{}'.format(keyword), unknown_brand, re.IGNORECASE)
        # start a counter to see if there were any brand matches. If not then we will 
        # set the brand to other which corresponds to the first element of a
        # one-hot array. Do not change 'other' from the last entry in the
        # 'brands' table
        if match:
            l.append(1)
            counter += 1
        else:
            l.append(0)
    if counter == 0:
        l[0] = 1
    return l

# main prediction function
def get_predicted_value(brand, item_type, title, est_price):
    brands_one_hot = create_one_hot_row(brand, ml_model.brands)

    item_types_query = "SELECT * FROM item_types;"
    item_types = [i[1] for i in engine.execute(item_types_query).fetchall()]
    item_types_one_hot = create_one_hot_row(item_type, item_types)
    print(item_types)

    adjectives_query = "SELECT * FROM item_adjectives;"
    adjectives = [a[1] for a in engine.execute(adjectives_query).fetchall()]
    adjectives_one_hot = create_one_hot_row_adj(title, adjectives)

    brands_query = "SELECT * FROM brands;"
    brands = [b[1] for b in engine.execute(brands_query).fetchall()]
    keywords = [b[2] for b in engine.execute(brands_query).fetchall()]
    brands_one_hot = create_one_hot_row_brand_keyword(brand, keywords)

    one_hot_row = brands_one_hot + item_types_one_hot + adjectives_one_hot + [est_price]

    # make columns
    columns = brands + item_types + adjectives + ['cost']
    input_df = pd.DataFrame(one_hot_row, columns)
    # take the exponent because the model was trained on the log of rent values
    prediction = np.exp(clf.predict(input_df.T)[0])
    return prediction

brand = 'Tibi'
item_type = "dresses"
title = 'Lurex Dress'
est_price = 10

print(get_predicted_value(brand, item_type, title, est_price))

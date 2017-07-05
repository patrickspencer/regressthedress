# -*- coding: utf-8 -*-
"""
    one_hot_funcs
    ~~~~~~~~~~~~~
    Functions used for data into one-hot arrays
"""

import os
import re
import pandas as pd
import numpy as np
from wombat.engine import ml_model
from sklearn.externals import joblib
from wombat.models import dbsession, engine, ItemAdjective, ItemType

reg_model_dir = os.path.dirname(os.path.abspath(__file__))
reg_model_path = os.path.join(reg_model_dir, 'stat_model_pickles',
        'rfr_v0.8_w_adj_prices_better_brands.pkl')

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

def one_hot_form_input(brand, item_type, title, est_price):
    """
    Returns pandas series
    """
    X_sample, _ = joblib.load(reg_model_path)
    print("x sample column #: {}".format(len(X_sample)))
    one_hot_array = X_sample
    one_hot_array['cost'] = est_price
    if brand in one_hot_array.index.values:
        one_hot_array[brand] = 1
    else:
        one_hot_array['other brand'] = 1
    if item_type in one_hot_array.index.values:
        one_hot_array[item_type] = 1
    else:
        pass

    adjectives_query = "SELECT * FROM item_adjectives;"
    adjectives = [a[1] for a in engine.execute(adjectives_query).fetchall()]
    for adj in adjectives:
        match = re.search('{}'.format(adj), title, re.IGNORECASE)
        if match:
            #l.append(1)
            try:
                one_hot_array[adj] = 1
            except TypeError:
                pass

    # take the exponent because the model was trained on the log of rent values
    # prediction = np.exp(reg.predict(input_df.T)[0])
    return one_hot_array

# used for debugging functions
# brand = 'Tibi'
# item_type = 'dresses'
# title = 'lurex dress'
# est_price = 300
# this = one_hot_form_input(brand = brand, item_type = item_type, title = title, est_price=est_price)
# print(len(this))

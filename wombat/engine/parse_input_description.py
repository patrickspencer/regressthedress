# -*- coding: utf-8 -*-
"""
    parse_input_description
    ~~~~~~~~~~~~~~~~~~~~~~~
    The main module for parsing input clothing item into pandas dataframes that
    can be used to find the price using our model.

    The user inputs the following: 'brand', 'item_type', 'title'. We search the
    title for words in a predetermined list of words like 'chiffon', or 'lace'.
    These words were used in creating our model.
"""

import os
import re
import pandas as pd
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
model = os.path.join(model_dir, 'stat_model_pickles', 'rfr_v0.3_with_adj.pkl')
clf = joblib.load(model)

# main prediction function
def get_predicted_value_rfr(brand, item_type, title):
    brands_one_hot = create_one_hot_row(brand, ml_model.brands)

    item_types_query = "SELECT * FROM item_types;"
    item_types = [i[1] for i in engine.execute(item_types_query).fetchall()]
    item_types_one_hot = create_one_hot_row(item_type, item_types)

    adjectives_query = "SELECT * FROM item_adjectives;"
    adjectives = [a[1] for a in engine.execute(adjectives_query).fetchall()]
    adjectives_one_hot = create_one_hot_row_adj(title, adjectives)

    one_hot_row = brands_one_hot + item_types_one_hot + adjectives_one_hot

    # make columns
    columns = ml_model.brands + item_types + adjectives
    input_df = pd.DataFrame(one_hot_row, columns)
    prediction = clf.predict(input_df.T)[0]
    return prediction
#
# brand = 'Tibi'
# item_type = "dresses"
# title = 'Lurex Dress'

# print(get_predicted_value(brand, item_type, title))

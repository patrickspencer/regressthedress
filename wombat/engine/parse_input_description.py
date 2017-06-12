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

import re
import pandas as pd
from wombat.engine import ml_model
from wombat.models import dbsession, ItemAdjective, ItemType

# get list of adjective features form database
features_adj = dbsession.query(ItemAdjective).all()
features_adj = [f.name for f in features_adj]

item_types = dbsession.query(ItemType).all()
item_types = [item.name for item in item_types]

brands = ml_model.brands

def create_one_hot_row_adj(sentence):
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
def create_one_hot_row(input_item_type, item_types):
    l = []
    for item in item_types:
        if input_item_type == item:                                       
            l.append(1)
        else:                                       
            l.append(0)
    return l

# sentence1 = 'Adrianna Papell Print Satin striped Handkerchief Dress shoulder'
# sentence2 = 'Micah Floral Silk Wrap Dress'
# print(create_one_hot_row_adj(sentence1))
# print(create_one_hot_row('dresses', item_types))
# print(create_one_hot_row('Nicole Miller', brands))

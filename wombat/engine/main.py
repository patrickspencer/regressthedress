import numpy as np
import jellyfish
from wombat.models import dbsession, Item
from sqlalchemy.dialects import postgresql

def get_top_n_similar_items(input_text,
        brand, 
        item_type, 
        method, 
        results_num = 10):
    """
    :param target_items: sqlalchemy objects with title attr
    :return: a tuple (l, q) where l is a list of sqlalchemy objects order from highest relevance to lowest relevance and q is the sql query that was used to search for these items
    """

    items = dbsession.query(Item).filter(
            Item.brand == brand, 
            Item.item_type == item_type)
    if not items:
        items = dbsession.query(Item).filter(
                Item.item_type == item_type)

    # we don't know which of the above outcomes will work so we'll save
    # the actual sql query to see where we got the information from.
    # actual_sql_query = items.statement.compile(dialect=postgresql.dialect())

    # compare distance of input_string to each item title
    d = {}

    for item in items.all():
        similarity_rating = jellyfish.levenshtein_distance(input_text, item.title)
        if not method or method == 'l':
            similarity_rating = jellyfish.levenshtein_distance(input_text, item.title)
        elif method == 'dl': 
            similarity_rating = jellyfish.damerau_levenshtein_distance(input_text, item.title)
        elif method == 'j': 
            similarity_rating = jellyfish.jaro_distance(input_text, item.title)
        elif method == 'jw': 
            similarity_rating = jellyfish.jaro_winkler(input_text, item.title)
        elif method == 'h': 
            similarity_rating = jellyfish.hamming_distance(input_text, item.title)

        # keep track of items with highest relevance in a dict d
        if len(d) <= results_num:
            d[item.id] = similarity_rating
        if max(d.values()) > similarity_rating:
            d[item.id] = similarity_rating
            d.pop(max(d, key=d.get), None)

    # sort the top values into a descending list
    list_of_ids = []
    while len(d) > 0:
        list_of_ids.append((min(d, key=d.get), min(d.values())))
        d.pop(min(d, key=d.get))

    # find items in database using their ids
    list_of_objects = []
    for i in list_of_ids:
        list_of_objects.append(dbsession.query(Item).filter(Item.id == i[0]).first())

    # return (new_l, actual_sql_query)
    return list_of_objects

def get_tight_avg(l):
    """
    Get average of numbers within on std dev of mean of list of numbers
    """
    l = np.array(l)
    stddev = np.std(l, 0)
    mean = np.mean(l, 0)
    new_l = []
    for i in l:
        if i > mean - stddev and i < mean + stddev:
            new_l.append(i)
    return new_l 

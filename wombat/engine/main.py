import numpy as np
import jellyfish
from wombat.models import dbsession, Item

def get_top_n_similar_items(input_text, results_num = 10):
    """
    :param target_items: sqlalchemy objects with title attr
    :return: a dictionary with entries of the form item_id: similarity_rating
    """

    items = dbsession.query(Item).filter(Item.item_type == 'dresses').all()

    # compare distance of input_string to each item title
    d = {}
    for item in items:
        similarity_rating = jellyfish.levenshtein_distance(input_text, item.title)
        # similarity_rating = fuzz.token_sort_ratio(input_text, item.title)
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
    # return np.mean(new_l, 0)
    return new_l

l = [398.0, 350.0, 179.0, 850.0, 224.0, 395.0, 247.99, 385.0, 208.0, 190.0, 189.0]
stddev = np.std(l)
print(np.std(l, 0))
mean = np.mean(l, 0)
print(np.mean(l))
new_l = []
for i in l:
    if i > mean - stddev and i < mean + stddev:
        new_l.append(i)
print(new_l)
print([i / 10 for i in new_l])

    

input_text = "Gown with Long Sleeves and Deep V"

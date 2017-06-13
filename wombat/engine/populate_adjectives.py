# -*- coding: utf-8 -*-
"""
    populate_features.py
    ~~~~~~~~~~~~~~~~~~~~
    This modules is used for the following purposes
    1.) Takes keywords from file key_words and inputs them into the database.
        These keywords are actually adjectives from the 'title' column in
        certain rows in the items db. We didn't want millions of adjectives so
        here 'certain' means just the first 100 rows in order to keep the
        number down
"""

from wombat.models import dbsession, engine, ItemAdjective, ItemType

f = open('key_words.txt', 'r')
key_words = f.read().split("\n") 
f.close() # close file

# function to see if a row already exsists in db and, if not, create the row
def get_or_create_adjective(name):
    instance = dbsession.query(ItemAdjective).filter(ItemAdjective.name == name).first()
    if instance:
        return instance, False
    else:
        instance = ItemAdjective(
                name = name,
        )
        dbsession.add(instance)
        dbsession.commit()
        return instance, True

# empty string is somehow a designer brand
banned_list = ['']

# populate item_features table in database from words in key_words.txt
for word in key_words:
    if word not in '':
        get_or_create_adjective(name = word)

# for testing to see if features works
adjectives = dbsession.query(ItemAdjective).all()

for adj in adjectives:
    print(adj.name)

# item types
def get_or_create_item_type(name):
    instance = dbsession.query(ItemType).filter(ItemType.name == name).first()
    if instance:
        return instance, False
    else:
        instance = ItemType(
                name = name,
        )
        dbsession.add(instance)
        dbsession.commit()
        return instance, True


item_types = engine.execute('SELECT DISTINCT item_type FROM items;').fetchall()
item_types = [r[0] for r in item_types]

for item_type in item_types:
    get_or_create_item_type(item_type)

# item types

def get_or_create_item_type(name):
    instance = dbsession.query(ItemType).filter(ItemType.name == name).first()
    if instance:
        return instance, False
    else:
        instance = ItemType(
                name = name,
        )
        dbsession.add(instance)
        dbsession.commit()
        return instance, True


item_types = engine.execute('SELECT DISTINCT item_type FROM items;').fetchall()
item_types = [r[0] for r in item_types]

for item_type in item_types:
    get_or_create_item_type(item_type)


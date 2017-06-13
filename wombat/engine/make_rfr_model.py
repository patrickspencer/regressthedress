import re
import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestRegressor
from wombat.models import dbsession, engine, ItemType, ItemAdjective
from wombat.engine import ml_model
from wombat.engine import parse_input_description as parse_title
from wombat.models import Item

df = ml_model.canonical_df

# get one-hot columns for brands 
dummy_brands = pd.get_dummies(df['brand'])
df = pd.concat([df, dummy_brands], axis = 1)
df = df.drop('brand', axis = 1)

# get one-hot columns for item_types
dummified_items = pd.get_dummies(df['item_type'])
df = pd.concat([df, dummified_items], axis = 1)
df = df.drop('item_type', axis = 1)
df_brands = df

# get list of adjective features form database
features_adj = [f.name for f in dbsession.query(ItemAdjective).all()]
item_types   = [item.name for item in dbsession.query(ItemType).all()]

# Make dummy variables for each item in df based on the adjectives that are
# contained in title
tokenized_titles = []
for title in df['title']:
    parse_title.create_one_hot_row_adj(title, features_adj)
    tokenized_titles.append(parse_title.create_one_hot_row_adj(title, features_adj))
df_adj = pd.DataFrame(tokenized_titles, columns = features_adj)
df_full = pd.concat([df_brands, df_adj], axis = 1)

# split data into train and test group
df = df_full
df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
train, test = df[df['is_train']==True], df[df['is_train']==False]

print('Number of observations in the training data:', len(train))
print('Number of observations in the test data:', len(test))

y = train['rent_per_week']
features = df_full.columns.drop(['rent_per_week', 'title']) # just column names

# make random forest model
clf = RandomForestRegressor()
clf.fit(train[features], train['rent_per_week'])

# make predictions
rfr_predicted = clf.predict(test[features]).astype(int)

# make predicted vs actual graph
fig, ax = plt.subplots(figsize=(20, 10))
y = test['rent_per_week']
test['rent_per_week'].max()
ax.scatter(x = test['rent_per_week'], y = rfr_predicted)
ax.plot([0, 200], [0, 200], 'k--', lw=4)
ax.set_xlabel('Measured', fontsize=18)
ax.set_ylabel('Predicted', fontsize=18)
y.max()
# plt.show()


import re
import pandas as pd
from wombat.models import dbsession, ItemFeature

features = dbsession.query(ItemFeature).filter(ItemFeature.category == 1).all()
for feature in features:
    print(feature.name)

adj_one_hot_df = pd.DataFrame

text = 'Adrianna Papell Print Satin striped Handkerchief Dress'
reg = r'(stripe)'
# for word in key_words:
#     match = re.search(reg, word, re.IGNORECASE) 
#     if match:
#         print(match.groups(0))

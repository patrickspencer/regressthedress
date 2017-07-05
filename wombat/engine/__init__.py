import re
import os
from wombat import models
from wombat.engine.main import *
from sklearn.externals import joblib
from wombat.engine.one_hot_funcs import reg_model_path

class Prediction(object):
    def __init__(self, brand, item_type, title, est_price):
        self.X_sample, self.reg = joblib.load(reg_model_path)
        self.sample_len = len(self.X_sample)
        self.brand = brand
        self.item_type = item_type
        self.title = title
        self.est_price = est_price

        # start flipping 'yes' switches depending on what the brand, item_type
        # and adjectives are in the input
        one_hot_array = self.X_sample
        one_hot_array['cost'] = self.est_price

        if self.brand in one_hot_array.index.values:
            one_hot_array[self.brand] = 1
        else:
            one_hot_array['other brand'] = 1
        if self.item_type in one_hot_array.index.values:
            one_hot_array[self.item_type] = 1
        else:
            pass
    
        adjectives_query = "SELECT * FROM item_adjectives;"
        adjectives = [a[1] for a in models.engine.execute(adjectives_query).fetchall()]
        for adj in adjectives:
            match = re.search('{}'.format(adj), self.title, re.IGNORECASE)
            if match:
                #l.append(1)
                try:
                    one_hot_array[adj] = 1
                except TypeError:
                    pass

        self.one_hot_array = one_hot_array
        self.one_hot_array_len = len(one_hot_array) 
        self.predicted_price = np.exp(self.reg.predict(self.one_hot_array))[0]
        self.predicted_price_str = '%.2f'%(np.exp(self.reg.predict(self.one_hot_array))[0])

        # get price range of similar items
        query = """
        SELECT rent_per_week 
        FROM items 
        WHERE 
            brand = '{}' and 
            item_type = '{}' and 
            cost > 0 and 
            cost < 5000;
        """.format(self.brand, self.item_type)
        
        res = models.engine.execute(query).fetchall()
        c = [r[0] for r in res]
        if len(c) != 0:
            self.price_range = (np.min(c), np.max(c))
        else:
            self.price_range = None

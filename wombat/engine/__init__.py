import re
import os
from wombat.models import engine
from wombat.engine.main import *
from sklearn.externals import joblib
from wombat.engine.one_hot_funcs import reg_model_path
from wombat.engine.one_hot_funcs import create_one_hot_row_adj, one_hot_form_input

def predict_price(brand, item_type, title, est_price):
    one_hot_series = one_hot_form_input(brand = brand,
            item_type = item_type, 
            title = title, 
            est_price = est_price)
    _, reg = joblib.load(reg_model_path)
    predicted_value = np.exp(reg.predict(one_hot_series))
    return predicted_value[0]

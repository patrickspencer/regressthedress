import re
import os
from sklearn.externals import joblib
from wombat.engine.main import *
from wombat.engine.one_hot_funcs import create_one_hot_row_adj
from wombat.engine.one_hot_funcs import one_hot_form_input
from wombat.models import engine

reg_model_dir = os.path.dirname(os.path.abspath(__file__))
reg_model_path = os.path.join(reg_model_dir, 'stat_model_pickles', 'rfr_v0.3_w_adj_prices_better_brands.pkl')

def predict_price(brand, item_type, title, est_price):
    one_hot_series = one_hot_form_input(brand = brand,
            item_type = item_type, 
            title = title, 
            est_price = est_price)
    _, reg = joblib.load(reg_model_path)
    predicted_value = np.exp(reg.predict(one_hot_series))
    return predicted_value[0]

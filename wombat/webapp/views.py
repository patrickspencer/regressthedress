import numpy as np
from wombat.engine import Prediction
from wombat.models import dbsession, Item
from wombat.webapp.forms import DescriptionForm
from wombat.models import engine, dbsession, Item
from flask import Blueprint, render_template, request, flash, send_from_directory
from wombat.engine.one_hot_funcs import one_hot_form_input
from wombat.engine.one_hot_funcs import reg_model_path
from sklearn.externals import joblib

main = Blueprint('main', __name__, url_prefix='/', static_folder='static')

@main.route("/", methods=['GET', 'POST'])
def index():
    form = DescriptionForm(request.form)
    predicted_value = ''
    price_range = None
    if request.method == 'POST' and form.validate():
        title = request.form['description']
        brand = request.form['brand']
        item_type = request.form['item_type']
        est_price = request.form['est_price']
        prediction = Prediction(brand = brand, item_type = item_type, est_price = est_price, title = title)
        predicted_value = '%.2f'%(prediction.predicted_price)
    return render_template('index.jinja2',
            form=form, prediction = prediction)

@main.route('robots.txt')
def static_from_root():
    return send_from_directory(main.static_folder, request.path[1:])

@main.route('about/')
def about():
    return render_template('about.jinja2')

@main.route('who/')
def who():
    return render_template('who.jinja2')

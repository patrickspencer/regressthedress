import numpy as np
from wombat import engine
from wombat.models import dbsession, Item
from wombat.webapp.forms import DescriptionForm
from flask import Blueprint, render_template, request
from wombat.engine.one_hot_funcs import one_hot_form_input
from wombat.engine import reg_model_path
from sklearn.externals import joblib

main = Blueprint('main', __name__, url_prefix='/')

@main.route("/", methods=['GET', 'POST'])
def index():
    form = DescriptionForm(request.form)
    predicted_value = ''
    if request.method == 'POST':
        title = request.form['description']
        brand = request.form['brand']
        item_type = request.form['item_type']
        est_price = request.form['est_price']

        predicted_value = engine.predict_price(brand = brand,
            item_type = item_type,
            title = title,
            est_price = est_price)
        predicted_value = '%.2f'%(predicted_value)

    return render_template('index.jinja2',
            form=form, predicted_value = predicted_value)

@main.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@main.route('/')
def input():
    return render_template('index.jinja2',
            form=form, predicted_value = predicted_value)

import numpy as np
from wombat import engine
from wombat.models import dbsession
from wombat.webapp.forms import DescriptionForm
from flask import Blueprint, render_template, request

main = Blueprint('main', __name__, url_prefix='/')

@main.route("/")
def index():
    form = DescriptionForm(request.form)
    return render_template('index.jinja2', form=form)

@main.route('finditem', methods=['GET', 'POST'])
def finditem():
    descr = request.form['description']
    similar_items = engine.main.get_top_n_similar_items(descr, request.form['brand'], request.form['item_type'], method="l")
    costs = [item.cost for item in similar_items]
    price_suggestion = np.median(np.array(costs)) / 10
    return render_template('results.jinja2', 
            similar_items = similar_items,
            costs = costs,
            price_suggestion = price_suggestion
            )

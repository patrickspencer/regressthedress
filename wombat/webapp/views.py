import numpy as np
from wombat import engine
from wombat.models import dbsession
from wombat.models import dbsession, Item
from wombat.webapp.forms import DescriptionForm
from flask import Blueprint, render_template, request
import matplotlib.pyplot as plt
from wombat.engine.parse_input_description import get_predicted_value_rfr

main = Blueprint('main', __name__, url_prefix='/')

@main.route("/", methods=['GET', 'POST'])
def index():
    form = DescriptionForm(request.form)
    predicted_value = ''
    if request.method == 'POST':
        title = request.form['description']
        brand = request.form['brand']
        item_type = request.form['item_type']
        predicted_value = get_predicted_value_rfr(brand, item_type, title)
    return render_template('index.jinja2',
            form=form, predicted_value = predicted_value)

@main.route('finditem', methods=['GET', 'POST'])
def finditem():
    descr = request.form['description']
    items = engine.main.get_top_n_similar_items(descr, request.form['brand'], request.form['item_type'], algorithm="l")
    similar_items = items[0]
    costs = [item.cost for item in similar_items]
    price_suggestion = np.median(np.array(costs)) / 10
    return render_template('results.jinja2',
            similar_items = similar_items,
            costs = costs,
            price_suggestion = price_suggestion,
            domain = items[1],
            all_prices = items[2]
            )

@main.route('plot', methods=['GET'])
def plot():
    if request.args['item_type'] and request.args['brand']:
        items = dbsession.query(Item).filter(
                Item.brand == request.args['brand'],
                Item.item_type == request.args['item_type'])
    elif request.args['item_type']:
        items = dbsession.query(Item).filter(
                Item.item_type == request.args['item_type'])
    c = [item.cost for item in items]
    # plt.boxplot(c)
    # plt.show()
    # fig = plt.figure()
    # canvas = FigureCanvas(fig)
    # output = StringIO.StringIO()
    # canvas.print_png(output)
    # response = make_response(output.getvalue())
    # response.mimetype = 'image/png'
    # return response

    return render_template('plot.jinja2', items=items)

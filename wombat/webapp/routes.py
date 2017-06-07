from wombat.models import dbsession
from wombat.webapp.forms import DescriptionForm
from flask import Blueprint, render_template, request

main = Blueprint('main', __name__, url_prefix='/')


@main.route("/")
def index():
    form = DescriptionForm(request.form)
    return render_template('index.jinja2', text=text, form=form)

@main.route('finditem', methods=['GET', 'POST'])
def finditem():
    result = request.form['description']
    return render_template('results.jinja2', result=result)

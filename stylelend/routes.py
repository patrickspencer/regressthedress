from flask import Blueprint, render_template
from stylelend.models import dbsession
main = Blueprint('main', __name__, url_prefix='/')

@main.route("/")
def index():
    return render_template('index.jinja2')

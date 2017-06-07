from flask import Flask
from wombat.webapp.views import main

def create_app():
    """
    Returns a Flask app given a configuration object

    :param config_object: a string which points to a class holding the
    configuration settings
    """
    app = Flask(__name__)
    app.config['DEBUG'] = True

    app.register_blueprint(main)

    return app

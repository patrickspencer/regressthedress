from flask import Flask

def create_app():
    """
    Returns a Flask app given a configuration object

    :param config_object: a string which points to a class holding the
    configuration settings
    """
    app = Flask(__name__)
    app.config['DEBUG'] = True

    from stylelend.routes import main

    app.register_blueprint(main)

    return app

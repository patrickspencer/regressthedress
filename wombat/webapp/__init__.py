from flask import Flask
from wombat.webapp.views import main

app = Flask(__name__)
app.register_blueprint(main)

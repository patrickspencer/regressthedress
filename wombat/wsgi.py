# This file is used by gunicorn (the production server) to invoke the Flask app
from wombat import webapp

if __name__ == "__main__":
    app = webapp.create_app()
    app.run(debug=False)

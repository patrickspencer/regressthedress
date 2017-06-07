# This file is used by gunicorn (the production server) to invoke the Flask app

from stylelend import settings
from stylelend.webapp import create_app

app = create_app()

if __name__ == "__main__":
    app.run()

# This file is used by gunicorn (the production server) to invoke the Flask app

if __name__ == "__main__":
    app = wombat.webapp.create_app()
    app.run()

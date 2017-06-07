from wombat import webapp

if __name__ == "__main__":
    app = webapp.create_app()
    app.run(debug=True)

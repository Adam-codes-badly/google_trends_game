from flask import Flask
from .db import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    with app.app_context():
        #initialise the database with the app
        db.init_app(app)
        # Import parts of our application
        from . import routes, models, config, forms
        # Register Blueprints or other configuration
        app.register_blueprint(routes.app)
        return app

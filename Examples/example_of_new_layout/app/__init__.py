from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

# Create the db object but do not initialize it just yet. Need this here for scope/used in other files like models.py
db = SQLAlchemy()


# Create a flask app. Pass in a config
def create_app(config_name):
    app = Flask(__name__)

    # Pulls in all our variables set in the config and adds them to the flask app
    app.config.from_object(config[config_name]())
    config[config_name].init_app(app)

    # Initializes the db object now that flask app object is made
    db.init_app(app)

    # Area for adding blueprints to our application
    # Adding blueprint from the main folder
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager


# Create the db object but do not initialize it just yet. Need this here for scope/used in other files like models.py
db = SQLAlchemy()


# Create the login manager object
login_manager = LoginManager()

# Point login view to the auth blueprint
login_manager.login_view = 'auth.login'


# Create a flask app. Pass in a config
def create_app(config_name):
    app = Flask(__name__)

    # Pulls in all our variables set in the config and adds them to the flask app
    app.config.from_object(config[config_name]())
    config[config_name].init_app(app)

    # Initializes the db object now that flask app object is made
    db.init_app(app)

    # Init the login object
    login_manager.init_app(app)

    # Area for adding blueprints to our application
    # Adding blueprint from the main folder
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Adding the Auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app

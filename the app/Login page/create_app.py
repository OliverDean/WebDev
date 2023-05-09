#create an instance of the flask app for testing purposes

from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from models import db



def create_app(config_name):
    print("Starting Flask application...")
    
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager = LoginManager(app)
    
    print("Flask application started.")
    
    return app

#create an instance of the flask app for testing purposes

from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from models import db
from app import register, login, logout, index, chat



def create_app(config_name):
    print("Starting Flask application...")
    
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager = LoginManager(app)
    app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])
    app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
    app.add_url_rule('/logout', 'logout', logout)
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/chat', 'chat', chat, methods=['POST'])
    
    print("Flask application started.")
    
    return app

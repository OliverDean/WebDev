from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
# from pyngrok import ngrok
from .error import init_app_error
from .config import Config
from dotenv import load_dotenv
from .seed_db import seed_questions
from .extensions import db

#db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

# Initialize the Flask application
app = Flask(__name__)
app.config.from_object(Config)
load_dotenv()
print("starting flask application...")

# Initialize the extensions
db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)
print("database initialized...")

init_app_error(app)
print("error handler initialized...")

from .models import User, UserSession, UserQuestionAnswer, Question
from .routes import main_bp

app.register_blueprint(main_bp)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()  # create the database
    seed_questions(app)  # seed the database

def create_test_app():
    app.config.from_object('config.TestingConfig') 
    with app.app_context():
        db.create_all() 
        seed_questions(app)
    return app

if __name__ == '__main__':
    app.run(debug=True)
    print("flask application started...")
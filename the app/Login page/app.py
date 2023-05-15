from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from .error import init_app_error
from .config import Config
from dotenv import load_dotenv
from .seed_db import seed_questions
from .extensions import db

#db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_class=Config):
    print("starting flask application...")
    load_dotenv()
    
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    print("database initialized...")


    
    init_app_error(app)
    print("error handler initialized...")

    from .models import User, UserSession, UserQuestionAnswer, Question
    from .routes import main_bp

    app.register_blueprint(main_bp)
    print("blueprint registered...")

    print("flask application started...")

    @login_manager.user_loader
    def load_user(user_id):
        print("load_user called")
        return User.query.get(int(user_id))

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()  # Create database tables for our data models
        seed_questions(app)  # seed the database
    app.run(debug=True)
    print("flask application started...")
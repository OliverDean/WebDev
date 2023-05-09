from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from email_validator import validate_email, EmailNotValidError
import string

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    sessions = relationship('UserSession', back_populates='user')
    question_answers = relationship('UserQuestionAnswer', back_populates='user')

    def set_password(self, password):
        if not all(c in string.printable for c in password):
            raise ValueError("Password cannot contain non-printable characters.")
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def set_email(self, email):
        try:
            v = validate_email(email)  # validate and get info
            email = v["email"]  # replace with normalized form
            self.email = email
        except EmailNotValidError as e:
            # email is not valid, exception message is human-readable
            print(str(e))
            raise ValueError("Invalid email format")
    
class UserSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    login_time = db.Column(db.DateTime, default=func.now())
    logout_time = db.Column(db.DateTime, nullable=True)
    duration = db.Column(db.Integer, nullable=True)

    user = relationship('User', back_populates='sessions')

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # the types can be replaced with the actual types, specific question classes
    question_type = db.Column(db.Enum('type 1', 'type 2', 'type 3', 'type 4'), nullable=False)
    submitted_answer = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())

    question_answers = relationship('UserQuestionAnswer', back_populates='question')

class UserQuestionAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    submitted_answer = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())

    user = relationship('User', back_populates='question_answers')
    question = relationship('Question', back_populates='question_answers')
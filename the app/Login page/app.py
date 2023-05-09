from flask import Flask, render_template, url_for, redirect, request, flash, jsonify
import secrets
import sys
from flask_sqlalchemy import SQLAlchemy
from requests import session
from sqlalchemy import func
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from datetime import datetime
from flask_migrate import Migrate

import openai

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.csrf import CSRFProtect
from flask_talisman import Talisman

from .main import get_openai_response
from .error import init_app_error
from .config import Config

from .models import User, UserSession, UserQuestionAnswer, Question, db

import re, string

print("starting flask application...")

app = Flask(__name__)
init_app_error(app)
print("error handler initialized.")
app.config.from_object(Config)
db.init_app(app)
# db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
print("flask application started.")

# @app.before_first_request
# def create_tables():
#    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    print("load_user called")
    return User.query.get(int(user_id))


# class RegistrationForm(FlaskForm):
#     username = StringField("Username", validators=[
#                            DataRequired(), Length(min=2, max=128)])
#     email = StringField("Email", validators=[DataRequired(), Email()])
#     password = PasswordField("Password", validators=[DataRequired()])
#     confirm_password = PasswordField("Confirm Password", validators=[
#                                      DataRequired(), EqualTo("password")])
#     submit = SubmitField("Sign Up")


# class LoginForm(FlaskForm):
#     username = StringField("Username", validators=[DataRequired()])
#     password = PasswordField("Password", validators=[DataRequired()])
#     submit = SubmitField("Login")


@login_manager.user_loader
def load_user(user_id):
    print("load_user called")
    return User.query.get(int(user_id))


@app.route('/')
def index():
    print('Index route called')
    return render_template('index.html')

# Might consider this implemtation later

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     print("Login route called")
#     form = LoginForm()
#     if form.validate_on_submit():
#         print('Login route - POST method')
#         username = form.username.data
#         password = form.password.data
#         user = User.query.filter_by(username=username).first()

#         if user and user.check_password(password):
#             login_user(user)
#             return jsonify(status="success")
#         else:
#             print('Login failed. Check your username and/or password.')
#             return jsonify(status="error", message="Login failed. Check your username and/or password.")
#     return render_template('dashboard.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("Login route called")
    if request.method == 'POST':
        print('Login route - POST method')
        username = request.form['login-username']
        password = request.form['login-password']
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return jsonify(status="success")
        else:
            print('Login failed. Check your username and/or password.')
            return jsonify(status="error", message="Login failed. Check your username and/or password.")
           
    return redirect(url_for('chatbot'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    print("Register route - start")
    if current_user.is_authenticated:
        print("Register route - user already authenticated")
        return redirect(url_for('index'))

    # form = RegistrationForm()
    # if form.validate_on_submit():
    #     print("Register route - POST method")
    #     username = form.username.data
    #     password = form.password.data
    #     email = form.email.data

    if request.method == 'POST':
        print("Register route - POST method")
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        email = request.form['email']

        print(
            f"Received form data: username={username}, email={email}, password={confirm_password}")
        
        if password != confirm_password:
            print('Passwords do not match.')
            return jsonify(status="error", message="Passwords do not match.")

        existing_user = User.query.filter_by(username=username).first()
        if existing_user is not None:
            return jsonify(status="error", message="Username already exists.")
        
        # Check for empty password
        if not password:
            return jsonify(status="error", message="Password cannot be empty.")

        # Check for valid email format
        email_regex = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(email_regex, email):
            return jsonify(status="error", message="Invalid email format.")

        # Check for long username
        if len(username) > 64:
            return jsonify(status="error", message="Username cannot be more than 64 characters.")

        # Check for non-printable username
        if not all(c in string.printable for c in username):
            return jsonify(status="error", message="Username cannot contain non-printable characters.")


        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        print("User registered")
        return jsonify(status="success")
    return render_template('index.html')


@app.route('/logout')
@login_required
def logout():
    user_session = UserSession.query.filter_by(
        user_id=session['user_id'], logout_time=None).first()
    if user_session:
        user_session.logout_time = func.now()
        db.session.commit()
    logout_user()
    flash('You have been logged out.', category='success')
    return redirect(url_for('index'))


@app.route('/users')
@login_required
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)



@app.route('/about')
def about():
    #todo we need a specific about page for the app describing what it is and does
    return render_template('about.html')



@app.route('/chatbot')
@login_required
def chatbot_login():
    #todo we need a specific about page for the app describing what it is and does
    return render_template('chatbot.html')

@app.route("/start", methods=["GET"])
@login_required
def start_chat():
    prompt = f"Return the initial statement:Hi, I'm Alice and we at Reli AI understand that dating is complicated. We want to help. What is your name?"

    response = openai.Completion.create(
        model="text-curie-001", # or whichever model you're using
        prompt=prompt,
        max_tokens=500,
    )

    return jsonify({
        "message": response.choices[0].text.strip()
    })


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json['message']

    # Here, you should write the logic for generating a prompt based on the user's message
    # For now, let's just use the user's message as the prompt
    prompt = user_message

    #response = openai.Completion.create(
    #    model="text-curie-001",
    #    prompt=prompt,
    #    max_tokens=60,
    #)

    #return jsonify({
    #    "message": response.choices[0].text.strip()
    #})

def get_openai_response(prompt):
    # Your code for generating the response using the OpenAI API
    pass

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)

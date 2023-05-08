from flask import Flask, render_template, url_for, redirect, request, flash, jsonify
import secrets
import sys
from flask_sqlalchemy import SQLAlchemy
from requests import session
from sqlalchemy import func
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from datetime import datetime
from flask_migrate import Migrate

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.csrf import CSRFProtect
from flask_talisman import Talisman

from .main import get_openai_response
from .error import init_app_error
from .config import Config

from .models import User, UserSession, UserQuestionAnswer, Question, db

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


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[
                           DataRequired(), Length(min=2, max=128)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[
                                     DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


@login_manager.user_loader
def load_user(user_id):
    print("load_user called")
    return User.query.get(int(user_id))


@app.route('/')
def index():
    print('Index route called')
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    print("Login route called")
    form = LoginForm()
    if form.validate_on_submit():
        print('Login route - POST method')
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return jsonify(status="success")
        else:
            print('Login failed. Check your username and/or password.')
            return jsonify(status="error", message="Login failed. Check your username and/or password.")
    return render_template('dashboard.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    print("Register route - start")
    if current_user.is_authenticated:
        print("Register route - user already authenticated")
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        print("Register route - POST method")
        username = form.username.data
        password = form.password.data
        email = form.email.data

        print(
            f"Received form data: username={username}, email={email}, password={password}")

        existing_user = User.query.filter_by(username=username).first()
        if existing_user is not None:
            return jsonify(status="error", message="Username already exists.")

        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        print("User registered")
        return jsonify(status="success")
    return render_template('index.html', form=form)


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


<<<<<<< HEAD
if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
=======
@app.route('/dashboard', methods=["GET", "POST"])
@login_required
def dashboard():
    result = ""
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        sex = request.form["sex"]
        interests = request.form["interests"]
        nationality = request.form["nationality"]
        humor_type = request.form["humor_type"]
        initialmeetingplace = request.form["initialmeetingplace"]

        result = get_openai_response(
            name, age, sex, interests, nationality, humor_type, initialmeetingplace)

    return render_template('dashboard.html', result=result)

>>>>>>> 7109eefdab6b9fd7ff4532debd263392b5cf15ca

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/start', methods=['GET', 'POST'])
def start():
    # todo
    return render_template('start.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    # todo
    return render_template('chat.html')


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)

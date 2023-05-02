from flask import Flask, render_template, url_for, redirect, request, flash, jsonify
from flask_mail import Mail, Message
from config import Config
import secrets, sys
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import LoginManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, login_required
from main import get_openai_response

print("starting flask application...")

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
print("flask application started.")

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=func.now())

    sessions = relationship('UserSession', back_populates='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
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


@app.before_first_request
def create_tables():
    db.create_all()


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
           
    return render_template('login.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    print("Register route - start")
    if current_user.is_authenticated:
        print("Register route - user already authenticated")
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        print("Register route - POST method")
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        email = request.form['email']

        print(f"Received form data: username={username}, email={email}, password={password}, confirm_password={confirm_password}")

        if password != confirm_password:
            print('Passwords do not match.')
            return jsonify(status="error", message="Passwords do not match.")

        existing_user = User.query.filter_by(username=username).first()
        if existing_user is not None:
            return jsonify(status="error", message="Username already exists.")

        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        print("User registered")
        return jsonify(status="success")
    return render_template('register.html')

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


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)

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
        
        result = get_openai_response(name, age, sex, interests, nationality, humor_type, initialmeetingplace)

    return render_template('dashboard.html', result=result)

@app.route('/about')
def about():
    return render_template('about.html')
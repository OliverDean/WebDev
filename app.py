from flask import Flask, render_template, url_for, redirect, request, flash, jsonify
from config import Config
import secrets, sys
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, login_required

print("starting flask application...")

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
print("flask application started.")

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

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
    logout_user()
    flash('You have been logged out.', category='success')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/users')
@login_required
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)

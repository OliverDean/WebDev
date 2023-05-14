from flask import Flask, render_template, url_for, redirect, request, flash, jsonify
import secrets
import sys
from flask_sqlalchemy import SQLAlchemy
from flask import session
from sqlalchemy import func
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from datetime import datetime
from flask_migrate import Migrate

import openai
import spacy

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.csrf import CSRFProtect
from flask_talisman import Talisman

from werkzeug.exceptions import BadRequest

from datetime import datetime


from .error import init_app_error
from .config import Config

from .models import User, UserSession, UserQuestionAnswer, Question, db

import re
import string

from .create_app import create_app

print("starting flask application...")

app = create_app()
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

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)



# # class RegistrationForm(FlaskForm):
# #     username = StringField("Username", validators=[
# #                            DataRequired(), Length(min=2, max=128)])
# #     email = StringField("Email", validators=[DataRequired(), Email()])
# #     password = PasswordField("Password", validators=[DataRequired()])
# #     confirm_password = PasswordField("Confirm Password", validators=[
# #                                      DataRequired(), EqualTo("password")])
# #     submit = SubmitField("Sign Up")


# # class LoginForm(FlaskForm):
# #     username = StringField("Username", validators=[DataRequired()])
# #     password = PasswordField("Password", validators=[DataRequired()])
# #     submit = SubmitField("Login")


# @app.route('/')
# def index():
#     print('Index route called')
#     return render_template('index.html')

# # Might consider this implemtation later

# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     print("Login route called")
# #     form = LoginForm()
# #     if form.validate_on_submit():
# #         print('Login route - POST method')
# #         username = form.username.data
# #         password = form.password.data
# #         user = User.query.filter_by(username=username).first()

# #         if user and user.check_password(password):
# #             login_user(user)
# #             return jsonify(status="success")
# #         else:
# #             print('Login failed. Check your username and/or password.')
# #             return jsonify(status="error", message="Login failed. Check your username and/or password.")
# #     return render_template('dashboard.html', form=form)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     print("Login route called")
#     if request.method == 'POST':
#         print('Login route - POST method')
#         username = request.form['login-username']
#         password = request.form['login-password']
#         user = User.query.filter_by(username=username).first()

#         if user and user.check_password(password):
#             login_user(user)
#             session['user_id'] = user.id  # Store user_id in the session
#             # Create a new UserSession record
#             new_session = UserSession(user_id=user.id)
#             db.session.add(new_session)  # Add the new record to the session
#             db.session.commit()  # Commit the changes to the database
#             return jsonify(status="success", message="Login successful."), 200
#         else:
#             print('Login failed. Check your username and/or password.')
#             return jsonify(status="error", message="Login failed. Check your username and/or password."), 400

#     return redirect(url_for('chatbot'))


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     print("Register route - start")
#     if current_user.is_authenticated:
#         print("Register route - user already authenticated")
#         return redirect(url_for('index'))

#     # form = RegistrationForm()
#     # if form.validate_on_submit():
#     #     print("Register route - POST method")
#     #     username = form.username.data
#     #     password = form.password.data
#     #     email = form.email.data

#     if request.method == 'POST':
#         print("Register route - POST method")
#         username = request.form['username']
#         password = request.form['password']
#         confirm_password = request.form['confirm_password']
#         email = request.form['email']

#         print(
#             f"Received form data: username={username}, email={email}, password={confirm_password}")

#         if password != confirm_password:
#             print('Passwords do not match.')
#             return jsonify(status="error", message="Passwords do not match."), 400

#         existing_user = User.query.filter_by(username=username).first()
#         if existing_user is not None:
#             print('Username already exists.')   
#             return jsonify(status="error", message="Username already exists."), 400

#         # Check for empty password
#         if not password:
#             return jsonify(status="error", message="Password cannot be empty."), 400

#         # Check for valid email format
#         email_regex = r"[^@]+@[^@]+\.[^@]+"
#         if not re.match(email_regex, email):
#             return jsonify(status="error", message="Invalid email format."), 400

#         # Check for long username
#         if len(username) > 64:
#             return jsonify(status="error", message="Username cannot be more than 64 characters."), 400

#         # Check for non-printable username
#         if not all(c in string.printable for c in username):
#             return jsonify(status="error", message="Username cannot contain non-printable characters."), 400

#         user = User(username=username, email=email)
#         user.set_password(password)
#         db.session.add(user)
#         db.session.commit()
#         print("User registered")
#         return jsonify(status="success", message="User registered."), 200
#     return render_template('index.html')


# @app.route('/logout')
# @login_required
# def logout():
#     user_session = UserSession.query.filter_by(
#         user_id=session['user_id'], logout_time=None).first()
#     if user_session:
#         user_session.logout_time = datetime.now()  # Record the logout time
#         db.session.commit()

#         # Calculate the session duration in seconds
#         user_session.duration = (
#             user_session.logout_time - user_session.login_time).total_seconds()
#         db.session.commit()

#     logout_user()
#     flash('You have been logged out.', category='success')
#     return redirect(url_for('index'))


# @app.route('/users')
# @login_required
# def users():
#     all_users = User.query.all()
#     return render_template('users.html', users=all_users)


# @app.route('/about')
# def about():
#     # todo we need a specific about page for the app describing what it is and does
#     return render_template('about.html')


# @app.route('/chatbot')
# @login_required
# def chatbot_login():
#     # todo we need a specific about page for the app describing what it is and does
#     return render_template('chatbot.html')


# @app.route("/start", methods=["GET"])
# @login_required
# def start_chat():
#     # prompt = f""

#     # response = openai.Completion.create(
#     #     model="text-curie-001",  # or whichever model you're using
#     #     prompt=prompt,
#     #     max_tokens=500,
#     # )

#     # return jsonify({
#     #     "message": response.choices[0].text.strip()
#     # })

#     session.clear()  # clear the session at the start of each chat
#     session["state"] = "get_name"  # set the initial state
#     response = "Hi, I'm Alice and we at Reli AI understand that dating is complicated. We want to help. What is your name?"
#     return jsonify({"message": response})


# @app.route("/chat", methods=["POST"])
# def chat():
#     user_message = request.json["message"].strip().capitalize()
#     response = ""
#     buttons = []

#     if session.get("state") == "get_name":
#         nlp = spacy.load("en_core_web_sm")
#         doc = nlp(user_message)
#         name = None
#         for ent in doc.ents:
#             if ent.label_ == "PERSON":
#                 name = ent.text
#                 break
#         if name:
#             session["name"] = name
#             session["saved_name"] = name
#             session["state"] = "get_age"
#             response = f"Hi {name}, are you over 18 years old? (yes/no)"
            
#         else:
#             session["name"] = user_message
#             session["saved_name"] = user_message
#             response = f"Hi {user_message}, What a name :), are you over 18 years old? (yes/no)"
#             session["state"] = "get_age"
            

#     elif session.get("state") == "get_age":
#         if user_message.lower().strip() == "yes":
#             session["state"] = "get_age_value"
#             response = "Great! How old/young are you?"
#         elif user_message.lower().strip() == "no":
#             session.clear()
#             response = "Sorry, you must be over 18 to use this service"
#         else:
#             response = "Please answer with 'yes' or 'no'"

#     elif session.get("state") == "get_age_value":
#         try:
#             age = int(user_message)
#             if age >= 18:
#                 session["age"] = age
#                 session["saved_age"] = age
#                 session["state"] = "permission_to_use"
#                 response = f"Thanks {session['saved_name']}, we at Reli AI understand that life is both too short, and too long to go without someone just for you. May we help you? (yes/no)"

#             else:
#                 session["age"] = age
#                 session["saved_age"] = age
#                 response = f"Sorry, {session['saved_name']} you must be over 18 to use this service :D"
#                 session["state"] = "session_end"
#         except ValueError:
#             response = "Please enter a valid age"

    
#     elif session.get("state") == "permission_to_use":
#         if user_message.lower().strip() == "yes":
#             response = f"Wonderful {session['saved_name']}, we will now ask you a series of questions designed to help us understand more about you, and may help you understand more about yourself. Shall we begin?"
#             session["state"] = "question_1"
#         elif user_message.lower().strip() == "no":
#             response = "Maybe another time :)"
#             session["state"] = "session_end"
#         else:
#             response = "Please answer with 'yes' or 'no'"

#     elif session.get("state") == "question_1":
#         if user_message.lower().strip() == "yes":
#             response = "Okay, great! Let's begin at the beginning. Who named you? and why that name? Tells us what you can."
#             session["name_background"] = user_message
#             session["state"] = "question_2"
#         elif user_message.lower().strip() == "no":
#             response = "Maybe another time :)"
#             session["state"] = "session_end"

#     elif session.get("state") == "question_2":
#         response = "what do you think life is about?"
#         session["question_life"] = user_message
#         session["state"] = "question_3"

#     elif session.get("state") == "question_3":
#         response = "What is love?"
#         session["question_love"] = user_message
#         session["state"] = "question_4"

#     elif session.get("state") == "question_4":
#         response = "What does it mean to be a parent?"
#         session["question_parent"] = user_message
#         session["state"] = "question_5"

#     elif session.get("state") == "question_5":
#         response = "What defines you as a person?"
#         session["question_life_definition"] = user_message
#         session["state"] = "question_6"

#     elif session.get("state") == "question_6":
#         response = "What is your favourite thing about yourself?"
#         session["question_favourite"] = user_message
#         session["state"] = "question_7"

#     elif session.get("state") == "question_7":
#         response = "What is your least favourite thing about yourself?"
#         session["question_least_favourite"] = user_message
#         session["state"] = "question_8"
    
#     elif session.get("state") == "question_8":
#         response = "Describe your ideal day alone."
#         session["question_solitude"] = user_message
#         session["state"] = "question_9"

#     elif session.get("state") == "question_9":
#         response = "Describe your ideal day with others."
#         session["question_social"] = user_message
#         session["state"] = "question_10"
    
#     elif session.get("state") == "question_10":
#         response = "What is your favourite thing to cook/eat?"
#         session["question_food"] = user_message
#         session["state"] = "question_11"

#     elif session.get("state") == "question_11":
#         response = "Do you like animals? If so, what is your favourite animal?"
#         session["question_animals"] = user_message
#         session["state"] = "question_12"

#     elif session.get("state") == "question_12":
#         response = "What does it mean to be a friend?"
#         session["question_friend"] = user_message
#         session["state"] = "question_13"
        
#     return jsonify({"message": response, "buttons": buttons})

# if __name__ == '__main__':
#     with app.app_context():
#         app.run(debug=True)

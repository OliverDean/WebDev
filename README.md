# WebDev
CITS3403 agile web development project

Work done by Oliver Dean 21307131 
and
Nick 

for the database 
pip install Flask-Migrate
if you dont see the app.db in the Login page directory then 
flask db init
if it is there but doesnt work try
flask db migrate -m "test"
flask db upgrade

i need to add some controls to the database as currently you can make a user profile with username r password r email r ...

login.html doesnt exist but is called by app.py might need to make a base case html
ERROR in app: Exception on /login [GET]
jinja2.exceptions.TemplateNotFound: login.html

ive updated the requirements.txt
pip install -r requirements.txt

need to flesh out these


the purpose of the web application, explaining the its design and use.
the architecture of the web application.
describe how to launch the web application.
describe some unit tests for the web application, and how to run them.
Include commit logs, showing contributions and review from both contributing students
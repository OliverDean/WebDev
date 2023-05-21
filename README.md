# WebDev
CITS3403 agile web development project

Work done by:
Oliver, 21307131 
and
Nick, 20262846


_the purpose of the web application, explaining the its design and use._

This Flask application is designed as a dating co pilot, it consists of multiple views that culminate in a chat tree with a bot that produces a dating profile.




In building our Flask application, we embraced Agile principles. We divided the project into a series of manageable sprints, on different components of the application. This approach allowed for faster testing and adaptations.

Throughout the process, clear and regular communication between the team was key to our success. After each sprint, we had meetings and discussions both in person and over discord.

Our application's features and design underwent constant evolution, as we were open to changes in response to the insights gained from iterative development and testing.

We also adopted continuous integration and continuous deployment. These allowed us to integrate regular code updates and conduct automated tests, minimizing errors.

Overall, using Agile principles allowed us to develop a high-quality, robust Flask application that that is modular and something we are both proud of.

This was a very challenging but rewarding project we both learnt a great deal.

_the architecture of the web application._


_describe how to launch the web application._

How to set up the flask app, in a terminal please write the following:

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

// Please run this from the Login page directory
flask run 

_describe some unit tests for the web application, and how to run them._

Running the selenium testing. from the Login page directory please run

python autoSelenium.py

For the unit testing please run 

python -m unittest testing.unitTests

If there is an error with the db seeding please run these commands in order

rm app.db
rm -r migrations/
flask db init
flask db migrate -m "upgrading"
flask db upgrade



_Include commit logs, showing contributions and review from both contributing students_

commit logs can be found in the log.txt file in this directory.
# WebDev
CITS3403 agile web development project

Work done by Oliver Dean 21307131 
and Nicholas Lim 20262846

___
Report

--
THE PURPOSE of the web application, explaining the its design and use.
--

Our app is designed to be part of the initial data collection process for a larger project where users are matchmade! based on their personality traits. It provides a good opportunity to think about how to make data collection a palatable experience for the user, dating in an online context and UX design as an overall concept.

The architecture of the web application.

This architecture follows the Model-View-Controller (MVC) pattern, where Flask handles the controller and routing aspects, SQLAlchemy manages the models and database interactions, and templates serve as the views for rendering HTML responses. 
The related components are as follows:

Flask: Flask is a micro web framework written in Python. It provides a foundation for building web applications by handling HTTP requests and responses, routing, and other web-related functionalities.

SQLAlchemy: SQLAlchemy is an Object-Relational Mapping (ORM) library that allows Python applications to interact with databases using object-oriented approaches. It provides a high-level API for working with database models, querying data, and performing database operations.

Database: The application uses a relational database, most likely supported by SQLAlchemy. The database stores persistent data, such as user information, session logs, question answers, and other application-specific data.

User Authentication: The application implements user authentication using the Flask-Login extension. It manages user sessions, user login, and user-related functionality.

Blueprints: The application organizes its routes and views using Flask blueprints. Blueprints allow modular structuring of the application by grouping related routes and views together.

Templates: The application likely uses HTML templates with Jinja2 templating engine to generate dynamic web pages. Templates help in separating the presentation logic from the application's business logic.

Static Files: The application includes static files such as CSS, JavaScript, and images for styling and client-side interactivity. These files are served by Flask to enhance the user interface and user experience.

Configuration: The application loads its configuration from a Config class, which may contain various settings such as database connection details, secret keys, and other environment-specific configurations.

Logging: The application utilizes logging to record important events and messages during its execution. Log statements are used to provide information, debug potential issues, and monitor the application's behavior.



--

DESCRIBE how to LAUNCH the web application.
--
Set up the environment:

Make sure you have Python installed on your machine.
Set up a virtual environment (optional but recommended) to isolate the application's dependencies.
Install dependencies:

Use a package manager like pip to install the required Python packages listed in the application's requirements.txt file. You can use the command pip install -r requirements.txt to install all the dependencies at once.
Set up the database:

Configure the database connection details in the application's configuration (e.g., Config class).
Run any necessary database migrations or initialization scripts to set up the required tables and schema.
Start the application:

Run the Flask application's entry point script (e.g., app.py or main.py) using the Python interpreter. Use the command python app.py or python main.py to start the application.
Access the web application:

By default, the web application will run on the Flask development server and be accessible at http://localhost:5000 in your web browser. If the port is different, it will be specified in the application's configuration.
Open the provided URL in your web browser to access and interact with the web application.


This Flask application is designed as a dating co pilot, it consists of multiple views that culminate in a chat tree with a bot that produces a dating profile.




In building our Flask application, we embraced Agile principles. We divided the project into a series of manageable sprints, on different components of the application. This approach allowed for faster testing and adaptations.

Throughout the process, clear and regular communication between the team was key to our success. After each sprint, we had meetings and discussions both in person and over discord.

Our application's features and design underwent constant evolution, as we were open to changes in response to the insights gained from iterative development and testing.

We also adopted continuous integration and continuous deployment. These allowed us to integrate regular code updates and conduct automated tests, minimizing errors.

Overall, using Agile principles allowed us to develop a high-quality, robust Flask application that that is modular and something we are both proud of.

This was a very challenging but rewarding project we both learnt a great deal.

--
Describe some UNIT TESTS for the web application, and how to run them.
--
These unit tests are written using the unittest framework in Python to test various functionalities and behaviors of the models in the application.

User Model Tests: These tests focus on the User model and cover scenarios such as creating a user, checking for unique usernames, validating passwords, handling invalid email formats, and other edge cases related to username and password length and non-printable characters.

User Session Model Tests: These tests target the UserSession model and check the creation of user sessions, ensuring a user is associated with a session, and verifying the ability to have multiple sessions for a user.

User Question Answer Model Tests: These tests concentrate on the UserQuestionAnswer model. They validate the creation of user question answers, checking for the presence of a user and a question, and testing the ability to have multiple answers for a user.

The tests are organized using the unittest.TestCase class, which provides methods like setUp (to set up test conditions), tearDown (to clean up after each test), and individual test methods (e.g., test_create_user, test_unique_username). Assertions are used to verify expected outcomes and ensure the behavior of the models aligns with the expectations.

To run these unit tests, execute the script by running python test_models.py from the command line. The unittest.main() function will discover and run all the test methods defined within the script. The test results will be displayed in the console, indicating whether each test passed or failed.

These tests help ensure that the models in the application behave correctly and handle various scenarios as expected, providing confidence in the reliability and correctness of the application's core functionalities related to user management, sessions, and question answers.



How to set up the flask app, in a terminal please write the following:

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

// Please run this from the Login page directory
flask run 

_describe some unit tests for the web application, and how to run them._


_Include commit logs, showing contributions and review from both contributing students_
___

___
Persistent bugs

Sometimes venv will simply not activate no matter what you try. Delete and restore the venv folder from recycle bin. This is a bug with venv and not the code.
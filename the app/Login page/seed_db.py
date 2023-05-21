from .extensions import db  # Import the db instance
from .models import Question


def seed_questions(app):
    with app.app_context():
        print("Seeding questions...")  # Check if the function is called
        try:
            # Check if the database is empty
            if not Question.query.first():
                # Seed the database with initial questions.
                questions = [
                    "Okay, great! Let's begin at the beginning. Who named you? and why that name? Tells us what you can.",
                    "what do you think life is about? What are you looking for?",
                    "What is love?",
                    "What does it mean to be a parent?",
                    "What defines you as a person?",
                    "What is your favourite thing about yourself?",
                    "What is your least favourite thing about yourself?",
                    "Describe your ideal day alone.",
                    "Describe your ideal day with others.",
                    "What is your favourite thing to cook/eat?",
                    "Do you like animals? If so, what is your favourite animal?",
                    "What does it mean to be a friend?",
                ]
                question_type = 'type 1'
                for question_text in questions:
                    question = Question(question_type=question_type, question_text=question_text)
                    db.session.add(question)
                db.session.commit()
                print("Database seeded with initial questions.")
            else:
                print("Database is not empty, not seeding questions.")  # Check if the conditional passes
        except Exception as e:
            print(f"Failed to query the database: {e}")  # Check if there's an error querying the database


from models import db, User, UserSession, Question, UserQuestionAnswer
import unittest
from create_app import create_app

class UserModelTest(unittest.TestCase):
    # executed prior to each test
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_user(self):
        """Test the creation of a User."""
        user = User(username='test', email='test@test.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        assert user in db.session
        assert user.check_password('password')

    def test_unique_username(self):
        """Test that creating a User with an existing username fails."""
        user1 = User(username='test', email='test1@test.com')
        user1.set_password('password')
        db.session.add(user1)
        db.session.commit()
        user2 = User(username='test', email='test2@test.com')
        user2.set_password('password')
        with self.assertRaises(Exception):
            db.session.add(user2)
            db.session.commit()

    def test_check_wrong_password(self):
        """Test that checking a wrong password returns False."""
        user = User(username='test', email='test@test.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        assert not user.check_password('wrong_password')

    def test_invalid_email(self):
        """Test that creating a User with an invalid email format fails."""
        user = User(username='test', email='invalid-email')
        user.set_password('password')
        with self.assertRaises(ValueError):
            db.session.add(user)
            db.session.commit()

    def test_missing_username(self):
        """Test that creating a User without a username fails."""
        user = User(email='test@test.com')
        user.set_password('password')
        with self.assertRaises(Exception):
            db.session.add(user)
            db.session.commit()

    def test_long_username(self):
        """Test that creating a User with a long username fails."""
        long_username = 'a' * 129  # create a string with 129 'a's
        user = User(username=long_username, email='test@test.com')
        user.set_password('password')
        with self.assertRaises(Exception):
            db.session.add(user)
            db.session.commit()

    def test_long_password(self):
        """Test that creating a User with a long password succeeds."""
        long_password = 'a' * 256  # create a string with 256 'a's
        user = User(username='test', email='test@test.com')
        user.set_password(long_password)
        db.session.add(user)
        db.session.commit()
        assert user.check_password(long_password)

    def test_non_printable_username(self):
        """Test that creating a User with a non-printable username fails."""
        user = User(username='\x00', email='test@test.com')  # '\x00' is a non-printable character
        user.set_password('password')
        with self.assertRaises(Exception):
            db.session.add(user)
            db.session.commit()

    def test_non_printable_password(self):
        """Test that creating a User with a non-printable password fails."""
        user = User(username='test', email='test@test.com')
        with self.assertRaises(ValueError):
            user.set_password('\x00')  # '\x00' is a non-printable character

    def test_create_user_without_username(self):
        """Test that creating a User without a username fails."""
        user = User(email='test@test.com')
        user.set_password('password')
        with self.assertRaises(Exception):
            db.session.add(user)
            db.session.commit()

    def test_create_user_without_email(self):
        """Test that creating a User without an email fails."""
        user = User(username='test')
        user.set_password('password')
        with self.assertRaises(Exception):
            db.session.add(user)
            db.session.commit()

    def test_create_user_without_password(self):
        """Test that creating a User without a password fails."""
        user = User(username='test', email='test@test.com')
        with self.assertRaises(Exception):
            db.session.add(user)
            db.session.commit()

    def test_set_password_after_creation(self):
        """Test setting a password after User creation."""
        user = User(username='test', email='test@test.com')
        db.session.add(user)
        db.session.commit()
        user.set_password('password')
        db.session.commit()
        assert user.check_password('password')

    def test_change_password(self):
        """Test changing a User's password."""
        user = User(username='test', email='test@test.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        user.set_password('new_password')
        db.session.commit()
        assert user.check_password('new_password')

    def test_check_password_with_different_case(self):
        """Test that checking a password with different case returns False."""
        user = User(username='test', email='test@test.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        assert not user.check_password('PASSWORD')

    def test_invalid_email(self):
        """Test that creating a User with an invalid email format fails."""
        user = User(username='test', email='invalid_email')
        user.set_password('password')
        with self.assertRaises(ValueError):
            db.session.add(user)
            db.session.commit()


class UserSessionModelTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_session(self):
        """Test the creation of a UserSession."""
        print('Running test_create_session...')
        user = User(username='test', email='test@test.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        session = UserSession(user_id=user.id)
        db.session.add(session)
        db.session.commit()
        self.assertIsNotNone(session.id)
        print('test_create_session passed.')

    def test_session_without_user(self):
        """Test that creating a UserSession without a User fails."""
        print('Running test_session_without_user...')
        session = UserSession()
        with self.assertRaises(Exception):
            db.session.add(session)
            db.session.commit()
        print('test_session_without_user passed.')

    def test_multiple_sessions_for_user(self):
        """Test that a User can have multiple sessions."""
        print('Running test_multiple_sessions_for_user...')
        user = User(username='test', email='test@test.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        session1 = UserSession(user_id=user.id)
        session2 = UserSession(user_id=user.id)
        db.session.add(session1)
        db.session.add(session2)
        db.session.commit()
        self.assertIsNotNone(session1.id)
        self.assertIsNotNone(session2.id)
        print('test_multiple_sessions_for_user passed.')

class UserQuestionAnswerModelTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_user_question_answer(self):
        """Test the creation of a UserQuestionAnswer."""
        print('Running test_create_user_question_answer...')
        user = User(username='test', email='test@test.com')
        user.set_password('password')
        question = Question(question_type='type 1', submitted_answer='answer')
        db.session.add(user)
        db.session.add(question)
        db.session.commit()
        user_question_answer = UserQuestionAnswer(user_id=user.id, question_id=question.id, submitted_answer='answer')
        db.session.add(user_question_answer)
        db.session.commit()
        self.assertIsNotNone(user_question_answer.id)
        print('test_create_user_question_answer passed.')

    def test_user_question_answer_without_user_or_question(self):
        """Test that creating a UserQuestionAnswer without a User or Question fails."""
        print('Running test_user_question_answer_without_user_or_question...')
        user_question_answer = UserQuestionAnswer(submitted_answer='answer')
        with self.assertRaises(Exception):
            db.session.add(user_question_answer)
            db.session.commit()
        print('test_user_question_answer_without_user_or_question passed.')

    def test_multiple_answers_for_user(self):
        """Test that a User can have multiple answers."""
        print('Running test_multiple_answers_for_user...')
        user = User(username='test', email='test@test.com')
        user.set_password('password')
        question1 = Question(question_type='type 1', submitted_answer='answer1')
        question2 = Question(question_type='type 2', submitted_answer='answer2')
        db.session.add(user)
        db.session.add(question1)
        db.session.add(question2)
        db.session.commit()
        answer1 = UserQuestionAnswer(user_id=user.id, question_id=question1.id, submitted_answer='answer1')
        answer2 = UserQuestionAnswer(user_id=user.id, question_id=question2.id, submitted_answer='answer2')
        db.session.add(answer1)
        db.session.add(answer2)
        db.session.commit()
        self.assertIsNotNone(answer1.id)
        self.assertIsNotNone(answer2.id)
        print('test_multiple_answers_for_user passed.')

if __name__ == '__main__':
    unittest.main()

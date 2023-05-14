"""empty message

<<<<<<<< HEAD:the app/Login page/migrations/versions/1efeeddc7d2e_test.py
Revision ID: 1efeeddc7d2e
Revises: 
Create Date: 2023-05-11 11:54:19.367185
========
Revision ID: 0f33cb99406c
Revises: 
Create Date: 2023-05-11 11:57:25.079717
>>>>>>>> d4ff905a54a45bf0b777d296cbb262ece31901e3:the app/Login page/migrations/versions/0f33cb99406c_.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<<< HEAD:the app/Login page/migrations/versions/1efeeddc7d2e_test.py
revision = '1efeeddc7d2e'
========
revision = '0f33cb99406c'
>>>>>>>> d4ff905a54a45bf0b777d296cbb262ece31901e3:the app/Login page/migrations/versions/0f33cb99406c_.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_type', sa.Enum('type 1', 'type 2', 'type 3', 'type 4'), nullable=False),
    sa.Column('submitted_answer', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('user_question_answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('submitted_answer', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_session',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('login_time', sa.DateTime(), nullable=True),
    sa.Column('logout_time', sa.DateTime(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_session')
    op.drop_table('user_question_answer')
    op.drop_table('user')
    op.drop_table('question')
    # ### end Alembic commands ###

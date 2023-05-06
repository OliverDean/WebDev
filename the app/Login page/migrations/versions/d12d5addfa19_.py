"""empty message

Revision ID: d12d5addfa19
Revises: de7376186b5b
Create Date: 2023-05-06 21:27:52.564850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd12d5addfa19'
down_revision = 'de7376186b5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question')
    op.drop_table('user')
    op.drop_table('user_question_answer')
    op.drop_table('user_session')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_session',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('login_time', sa.DATETIME(), nullable=True),
    sa.Column('logout_time', sa.DATETIME(), nullable=True),
    sa.Column('duration', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_question_answer',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('question_id', sa.INTEGER(), nullable=False),
    sa.Column('submitted_answer', sa.TEXT(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=128), nullable=False),
    sa.Column('email', sa.VARCHAR(length=128), nullable=False),
    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('question',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('question_type', sa.VARCHAR(length=6), nullable=False),
    sa.Column('submitted_answer', sa.TEXT(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###

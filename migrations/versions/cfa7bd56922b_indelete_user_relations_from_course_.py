"""Indelete user relations from course class

Revision ID: cfa7bd56922b
Revises: da892a07683e
Create Date: 2022-05-19 23:36:16.380957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfa7bd56922b'
down_revision = 'da892a07683e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('courses_user_id_fkey', 'courses', type_='foreignkey')
    op.drop_column('courses', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('courses', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('courses_user_id_fkey', 'courses', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###

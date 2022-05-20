"""add password harsh to user object

Revision ID: c67a132eabf7
Revises: 6f432e0b8d9c
Create Date: 2022-05-20 00:51:29.291443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c67a132eabf7'
down_revision = '6f432e0b8d9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###

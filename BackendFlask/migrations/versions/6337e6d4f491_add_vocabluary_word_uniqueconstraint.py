"""add vocabluary word UniqueConstraint

Revision ID: 6337e6d4f491
Revises: 32b1d801d740
Create Date: 2020-03-25 14:37:33.115027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6337e6d4f491'
down_revision = '32b1d801d740'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uix_word', 'vocabulary', ['word'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uix_word', 'vocabulary', type_='unique')
    # ### end Alembic commands ###

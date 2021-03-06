"""add word frequency

Revision ID: 3e74790c0d3c
Revises: 91dcf21a8796
Create Date: 2020-03-24 22:31:03.235368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e74790c0d3c'
down_revision = '91dcf21a8796'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vocabdata', sa.Column('frequency', sa.Integer(), nullable=False))
    op.add_column('vocabulary', sa.Column('frequency', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vocabulary', 'frequency')
    op.drop_column('vocabdata', 'frequency')
    # ### end Alembic commands ###

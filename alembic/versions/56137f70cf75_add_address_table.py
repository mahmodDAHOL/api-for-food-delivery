"""add address table

Revision ID: 56137f70cf75
Revises: 256a425a84b2
Create Date: 2022-05-17 00:13:39.926312

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '56137f70cf75'
down_revision = '256a425a84b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('addressType', sa.String(), nullable=False),
    sa.Column('contactPersonName', sa.String(), nullable=False),
    sa.Column('contactPersonNumber', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('latitude', sa.String(), nullable=False),
    sa.Column('longitude', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('addressType')
    )



def downgrade():

    op.drop_table('addresses')
"""add phone and name columns

Revision ID: e5534e9ee0a2
Revises: c47ecbf163d4
Create Date: 2022-05-05 00:38:41.247169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5534e9ee0a2'
down_revision = 'c47ecbf163d4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('phone', sa.String(), nullable=False))
    op.add_column('users', sa.Column('name', sa.String(), nullable=False))



def downgrade():
    op.drop_column('users', 'phone')
    op.drop_column('users', 'name')


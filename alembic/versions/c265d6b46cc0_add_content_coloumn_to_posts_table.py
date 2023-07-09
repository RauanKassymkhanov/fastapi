"""add content coloumn to posts table

Revision ID: c265d6b46cc0
Revises: f5fbf5408708
Create Date: 2023-07-07 23:57:34.523492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c265d6b46cc0'
down_revision = 'f5fbf5408708'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts',  'content')
    pass

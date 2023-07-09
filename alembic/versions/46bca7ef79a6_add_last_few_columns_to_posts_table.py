"""add last few columns to posts table

Revision ID: 46bca7ef79a6
Revises: 83da9d8dc22d
Create Date: 2023-07-08 00:15:35.387800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46bca7ef79a6'
down_revision = '83da9d8dc22d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
                  sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts',
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')

    pass

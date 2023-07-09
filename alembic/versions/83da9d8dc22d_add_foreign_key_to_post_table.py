"""add foreign key to post table

Revision ID: 83da9d8dc22d
Revises: cdb863f43125
Create Date: 2023-07-08 00:09:58.634247

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83da9d8dc22d'
down_revision = 'cdb863f43125'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass

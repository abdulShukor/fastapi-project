"""add foreign-key to posts table

Revision ID: 331bd12312b2
Revises: 0632f8852364
Create Date: 2023-06-17 22:11:06.633444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '331bd12312b2'
down_revision = '0632f8852364'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass

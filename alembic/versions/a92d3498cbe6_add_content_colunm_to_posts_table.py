"""add content colunm to posts table

Revision ID: a92d3498cbe6
Revises: 0bf8c563e1a5
Create Date: 2023-06-17 21:59:26.129765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a92d3498cbe6'
down_revision = '0bf8c563e1a5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass

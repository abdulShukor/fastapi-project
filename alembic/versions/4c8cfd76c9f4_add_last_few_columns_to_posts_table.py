"""add last few columns to posts table

Revision ID: 4c8cfd76c9f4
Revises: 331bd12312b2
Create Date: 2023-06-17 22:15:26.888462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c8cfd76c9f4'
down_revision = '331bd12312b2'
branch_labels = None
depends_on = None



def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass

"""added content colunm to post table

Revision ID: 409fb16a5ccc
Revises: ce285c11a0f6
Create Date: 2023-06-15 21:28:07.664926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '409fb16a5ccc'
down_revision = 'ce285c11a0f6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass

"""add user table

Revision ID: a5a3fd1cd443
Revises: 409fb16a5ccc
Create Date: 2023-06-15 21:35:24.497155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5a3fd1cd443'
down_revision = '409fb16a5ccc'
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')

    pass

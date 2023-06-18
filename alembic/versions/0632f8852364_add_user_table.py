"""add user table

Revision ID: 0632f8852364
Revises: a92d3498cbe6
Create Date: 2023-06-17 22:07:13.086340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0632f8852364'
down_revision = 'a92d3498cbe6'
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
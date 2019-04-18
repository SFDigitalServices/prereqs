"""add is_admin column to user table

Revision ID: cbd2fa252c24
Revises: f78459e65a0d
Create Date: 2019-04-18 10:04:29.019762

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import expression


# revision identifiers, used by Alembic.
revision = 'cbd2fa252c24'
down_revision = 'f78459e65a0d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user',
        sa.Column('is_admin', sa.Boolean(), nullable=False, server_default=expression.false())
    )


def downgrade():
    op.drop_column('user', 'is_admin')

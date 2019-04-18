"""create user table

Revision ID: 3a2b72e84ac0
Revises: 
Create Date: 2019-04-03 14:53:46.509743

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '3a2b72e84ac0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', UUID(), primary_key=True, server_default=sa.text("uuid_generate_v4()")),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('secret', sa.String(2048))
    )


def downgrade():
    op.drop_table('user')

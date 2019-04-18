"""create group table

Revision ID: 5a31516650ab
Revises: 3a2b72e84ac0
Create Date: 2019-04-04 16:43:05.213251

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '5a31516650ab'
down_revision = '3a2b72e84ac0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'group',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False)
    )

    op.create_table(
        'user_group',
        sa.Column('user_id', UUID(), nullable=False),
        sa.Column('group_id', sa.Integer, nullable=False)
    )

    op.create_foreign_key(
        'fk_user_id',
        'user_group',
        'user',
        ['user_id'],
        ['id']
    )

    op.create_foreign_key(
        'fk_group_id',
        'user_group',
        'group',
        ['group_id'],
        ['id']
    )


def downgrade():
    op.drop_table('group')
    op.drop_table('user_group')


"""create approval tables

Revision ID: f78459e65a0d
Revises: 5a31516650ab
Create Date: 2019-04-05 09:59:29.351173

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = 'f78459e65a0d'
down_revision = '5a31516650ab'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'approval',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('created_by', UUID()),
        sa.Column('last_modified_by', UUID()),
        sa.Column('last_modified_date', sa.DateTime)
    )

    op.create_table(
        'prereq',
        sa.Column('approval_id', sa.Integer, nullable=False),
        sa.Column('prereq_id', sa.Integer, nullable=False)
    )

    op.create_table(
        'request',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('approval_id', sa.Integer, nullable=False),
        sa.Column('data', sa.JSON),
        sa.Column('status', sa.String(100)),
        sa.Column('root_request_id', sa.Integer),
        sa.Column('parent_request_id', sa.Integer),
        sa.Column('owner_id', UUID())
    )

    op.create_foreign_key(
        'fk_approval_last_modified_by',
        'approval',
        'user_account',
        ['last_modified_by'],
        ['id']
    )
    op.create_foreign_key(
        'fk_approval_created_by',
        'approval',
        'user_account',
        ['created_by'],
        ['id']
    )

    op.create_primary_key(
        'pk_prereq',
        'prereq',
        ['approval_id', 'prereq_id']
    )
    op.create_foreign_key(
        'fk_prereq_approval_id',
        'prereq',
        'approval',
        ['approval_id'],
        ['id']
    )
    op.create_foreign_key(
        'fk_prereq_prereq_id',
        'prereq',
        'approval',
        ['prereq_id'],
        ['id']
    )

    op.create_foreign_key(
        'fk_request_approval_id',
        'request',
        'approval',
        ['approval_id'],
        ['id']
    )
    op.create_foreign_key(
        'fk_request_root_request_id',
        'request',
        'request',
        ['root_request_id'],
        ['id']
    )
    op.create_foreign_key(
        'fk_request_parent_request_id',
        'request',
        'request',
        ['parent_request_id'],
        ['id']
    )
    op.create_foreign_key(
        'fk_request_owner_id',
        'request',
        'user_account',
        ['owner_id'],
        ['id']
    )


def downgrade():
    op.drop_table('approval')
    op.drop_table('prereq')
    op.drop_table('request')

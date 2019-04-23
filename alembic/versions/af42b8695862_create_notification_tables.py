"""create notification tables

Revision ID: af42b8695862
Revises: cbd2fa252c24
Create Date: 2019-04-23 13:29:30.012407

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = 'af42b8695862'
down_revision = 'cbd2fa252c24'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'event_notification',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('event', sa.String(100), nullable=False),
        sa.Column('script_path', sa.String(1024), nullable=False)
    )

    op.create_table(
        'approval_notification',
        sa.Column('approval_id', sa.Integer, nullable=False),
        sa.Column('event_notification_id', sa.Integer, nullable=False),
        sa.Column('variables', sa.JSON)
    )

    op.create_table(
        'request_notification',
        sa.Column('request_id', sa.Integer, nullable=False),
        sa.Column('event_notification_id', sa.Integer, nullable=False),
        sa.Column('variables', sa.JSON)
    )

    op.create_table(
        'notification_log',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', UUID(), nullable=False),
        sa.Column('date_sent', sa.DateTime, server_default=sa.func.current_timestamp()),
        sa.Column('content', sa.Text)
    )

    op.create_foreign_key(
        'fk_approval_notification_approval_id',
        'approval_notification',
        'approval',
        ['approval_id'],
        ['id']
    )

    op.create_foreign_key(
        'fk_approval_notification_event_notification_id',
        'approval_notification',
        'event_notification',
        ['event_notification_id'],
        ['id']
    )

    op.create_foreign_key(
        'fk_request_notification_request_id',
        'request_notification',
        'request',
        ['request_id'],
        ['id']
    )

    op.create_foreign_key(
        'fk_request_notification_event_notification_id',
        'request_notification',
        'event_notification',
        ['event_notification_id'],
        ['id']
    )

    op.create_foreign_key(
        'fk_notification_log_user_id',
        'notification_log',
        'user',
        ['user_id'],
        ['id']
    )

def downgrade():
    op.drop_table('request_notification')
    op.drop_table('approval_notification')
    op.drop_table('event_notification')

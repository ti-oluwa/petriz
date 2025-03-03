"""empty message

Revision ID: 9ea8f5fd9599
Revises: 6e9c404176a0
Create Date: 2025-03-02 23:36:45.116468

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision: str = '9ea8f5fd9599'
down_revision: Union[str, None] = '6e9c404176a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audits__audit_log_entries',
    sa.Column('uid', sa.String(length=50), nullable=False),
    sa.Column('event', sa.String(length=255), nullable=False),
    sa.Column('source', sa.String(length=255), nullable=False),
    sa.Column('actor_id', sa.String(length=50), nullable=False),
    sa.Column('actor_type', sa.String(length=50), nullable=False),
    sa.Column('account_email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=True),
    sa.Column('account_id', sa.UUID(), nullable=True),
    sa.Column('target', sa.String(length=255), nullable=True),
    sa.Column('target_id', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('status', sa.Enum('SUCCESS', 'ERROR', name='actionstatus'), nullable=False),
    sa.Column('data', sa.JSON(), nullable=True),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_audit_logentry_created_at', 'audits__audit_log_entries', ['created_at'], unique=False)
    op.create_index('ix_audit_logentry_updated_at', 'audits__audit_log_entries', ['updated_at'], unique=False)
    op.create_index(op.f('ix_audits__audit_log_entries_account_email'), 'audits__audit_log_entries', ['account_email'], unique=False)
    op.create_index(op.f('ix_audits__audit_log_entries_account_id'), 'audits__audit_log_entries', ['account_id'], unique=False)
    op.create_index(op.f('ix_audits__audit_log_entries_actor_id'), 'audits__audit_log_entries', ['actor_id'], unique=False)
    op.create_index(op.f('ix_audits__audit_log_entries_actor_type'), 'audits__audit_log_entries', ['actor_type'], unique=False)
    op.create_index(op.f('ix_audits__audit_log_entries_event'), 'audits__audit_log_entries', ['event'], unique=False)
    op.create_index(op.f('ix_audits__audit_log_entries_id'), 'audits__audit_log_entries', ['id'], unique=False)
    op.create_index(op.f('ix_audits__audit_log_entries_source'), 'audits__audit_log_entries', ['source'], unique=False)
    op.create_index(op.f('ix_audits__audit_log_entries_status'), 'audits__audit_log_entries', ['status'], unique=False)
    op.create_index(op.f('ix_audits__audit_log_entries_target'), 'audits__audit_log_entries', ['target'], unique=False)
    op.create_index(op.f('ix_audits__audit_log_entries_target_id'), 'audits__audit_log_entries', ['target_id'], unique=False)
    op.create_index(op.f('ix_audits__audit_log_entries_uid'), 'audits__audit_log_entries', ['uid'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_audits__audit_log_entries_uid'), table_name='audits__audit_log_entries')
    op.drop_index(op.f('ix_audits__audit_log_entries_target_id'), table_name='audits__audit_log_entries')
    op.drop_index(op.f('ix_audits__audit_log_entries_target'), table_name='audits__audit_log_entries')
    op.drop_index(op.f('ix_audits__audit_log_entries_status'), table_name='audits__audit_log_entries')
    op.drop_index(op.f('ix_audits__audit_log_entries_source'), table_name='audits__audit_log_entries')
    op.drop_index(op.f('ix_audits__audit_log_entries_id'), table_name='audits__audit_log_entries')
    op.drop_index(op.f('ix_audits__audit_log_entries_event'), table_name='audits__audit_log_entries')
    op.drop_index(op.f('ix_audits__audit_log_entries_actor_type'), table_name='audits__audit_log_entries')
    op.drop_index(op.f('ix_audits__audit_log_entries_actor_id'), table_name='audits__audit_log_entries')
    op.drop_index(op.f('ix_audits__audit_log_entries_account_id'), table_name='audits__audit_log_entries')
    op.drop_index(op.f('ix_audits__audit_log_entries_account_email'), table_name='audits__audit_log_entries')
    op.drop_index('ix_audit_logentry_updated_at', table_name='audits__audit_log_entries')
    op.drop_index('ix_audit_logentry_created_at', table_name='audits__audit_log_entries')
    op.drop_table('audits__audit_log_entries')
    # ### end Alembic commands ###

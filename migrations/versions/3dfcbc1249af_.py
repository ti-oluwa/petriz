"""empty message

Revision ID: 3dfcbc1249af
Revises: 5dcc9e8523d1
Create Date: 2024-11-30 23:23:30.371421

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '3dfcbc1249af'
down_revision: Union[str, None] = '5dcc9e8523d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('applications__applications',
    sa.Column('uid', sa.String(length=50), nullable=True),
    sa.Column('name', sa.Unicode(length=255), nullable=True),
    sa.Column('authentication_type', sa.Enum('AUTH_TOKEN', 'ACCESS_KEY', name='applicationauthenticationtype'), nullable=True),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_applications__applications_id'), 'applications__applications', ['id'], unique=False)
    op.create_index(op.f('ix_applications__applications_uid'), 'applications__applications', ['uid'], unique=True)
    op.create_table('tokens__access_keys',
    sa.Column('account_id', sa.UUID(), nullable=False),
    sa.Column('secret', sa.String(length=50), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('valid_until', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['accounts__client_accounts.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('account_id', 'secret')
    )
    op.create_index(op.f('ix_tokens__access_keys_account_id'), 'tokens__access_keys', ['account_id'], unique=False)
    op.create_index(op.f('ix_tokens__access_keys_id'), 'tokens__access_keys', ['id'], unique=False)
    op.create_index(op.f('ix_tokens__access_keys_is_active'), 'tokens__access_keys', ['is_active'], unique=False)
    op.create_index(op.f('ix_tokens__access_keys_secret'), 'tokens__access_keys', ['secret'], unique=False)
    op.create_table('tokens__api_keys',
    sa.Column('secret', sa.String(length=100), nullable=False),
    sa.Column('application_id', sa.UUID(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('valid_until', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['application_id'], ['applications__applications.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('application_id', 'secret')
    )
    op.create_index(op.f('ix_tokens__api_keys_application_id'), 'tokens__api_keys', ['application_id'], unique=False)
    op.create_index(op.f('ix_tokens__api_keys_id'), 'tokens__api_keys', ['id'], unique=False)
    op.create_index(op.f('ix_tokens__api_keys_is_active'), 'tokens__api_keys', ['is_active'], unique=False)
    op.create_index(op.f('ix_tokens__api_keys_secret'), 'tokens__api_keys', ['secret'], unique=False)
    op.create_table('tokens__auth_tokens',
    sa.Column('account_id', sa.UUID(), nullable=False),
    sa.Column('secret', sa.String(length=50), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('valid_until', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['accounts__client_accounts.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('account_id', 'secret')
    )
    op.create_index(op.f('ix_tokens__auth_tokens_account_id'), 'tokens__auth_tokens', ['account_id'], unique=False)
    op.create_index(op.f('ix_tokens__auth_tokens_id'), 'tokens__auth_tokens', ['id'], unique=False)
    op.create_index(op.f('ix_tokens__auth_tokens_is_active'), 'tokens__auth_tokens', ['is_active'], unique=False)
    op.create_index(op.f('ix_tokens__auth_tokens_secret'), 'tokens__auth_tokens', ['secret'], unique=False)
    op.drop_index('ix_accounts__client_access_keys_account_id', table_name='accounts__client_access_keys')
    op.drop_index('ix_accounts__client_access_keys_id', table_name='accounts__client_access_keys')
    op.drop_index('ix_accounts__client_access_keys_is_active', table_name='accounts__client_access_keys')
    op.drop_index('ix_accounts__client_access_keys_secret', table_name='accounts__client_access_keys')
    op.drop_table('accounts__client_access_keys')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts__client_access_keys',
    sa.Column('account_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('secret', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['accounts__client_accounts.id'], name='accounts__client_access_keys_account_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='accounts__client_access_keys_pkey'),
    sa.UniqueConstraint('account_id', 'secret', name='accounts__client_access_keys_account_id_secret_key')
    )
    op.create_index('ix_accounts__client_access_keys_secret', 'accounts__client_access_keys', ['secret'], unique=False)
    op.create_index('ix_accounts__client_access_keys_is_active', 'accounts__client_access_keys', ['is_active'], unique=False)
    op.create_index('ix_accounts__client_access_keys_id', 'accounts__client_access_keys', ['id'], unique=False)
    op.create_index('ix_accounts__client_access_keys_account_id', 'accounts__client_access_keys', ['account_id'], unique=False)
    op.drop_index(op.f('ix_tokens__auth_tokens_secret'), table_name='tokens__auth_tokens')
    op.drop_index(op.f('ix_tokens__auth_tokens_is_active'), table_name='tokens__auth_tokens')
    op.drop_index(op.f('ix_tokens__auth_tokens_id'), table_name='tokens__auth_tokens')
    op.drop_index(op.f('ix_tokens__auth_tokens_account_id'), table_name='tokens__auth_tokens')
    op.drop_table('tokens__auth_tokens')
    op.drop_index(op.f('ix_tokens__api_keys_secret'), table_name='tokens__api_keys')
    op.drop_index(op.f('ix_tokens__api_keys_is_active'), table_name='tokens__api_keys')
    op.drop_index(op.f('ix_tokens__api_keys_id'), table_name='tokens__api_keys')
    op.drop_index(op.f('ix_tokens__api_keys_application_id'), table_name='tokens__api_keys')
    op.drop_table('tokens__api_keys')
    op.drop_index(op.f('ix_tokens__access_keys_secret'), table_name='tokens__access_keys')
    op.drop_index(op.f('ix_tokens__access_keys_is_active'), table_name='tokens__access_keys')
    op.drop_index(op.f('ix_tokens__access_keys_id'), table_name='tokens__access_keys')
    op.drop_index(op.f('ix_tokens__access_keys_account_id'), table_name='tokens__access_keys')
    op.drop_table('tokens__access_keys')
    op.drop_index(op.f('ix_applications__applications_uid'), table_name='applications__applications')
    op.drop_index(op.f('ix_applications__applications_id'), table_name='applications__applications')
    op.drop_table('applications__applications')
    # ### end Alembic commands ###
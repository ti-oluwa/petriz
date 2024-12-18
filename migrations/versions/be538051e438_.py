"""empty message

Revision ID: be538051e438
Revises: 879da84bd87e
Create Date: 2024-12-04 10:45:22.233520

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'be538051e438'
down_revision: Union[str, None] = '879da84bd87e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_tokens__access_keys_account_id', table_name='tokens__access_keys')
    op.drop_index('ix_tokens__access_keys_id', table_name='tokens__access_keys')
    op.drop_index('ix_tokens__access_keys_is_active', table_name='tokens__access_keys')
    op.drop_index('ix_tokens__access_keys_secret', table_name='tokens__access_keys')
    op.drop_table('tokens__access_keys')
    op.drop_index('ix_clients__clients_id', table_name='clients__clients')
    op.drop_index('ix_clients__clients_uid', table_name='clients__clients')
    op.drop_index('ix_tokens__api_keys_client_id', table_name='tokens__api_keys')
    op.drop_index('ix_tokens__api_keys_id', table_name='tokens__api_keys')
    op.drop_index('ix_tokens__api_keys_is_active', table_name='tokens__api_keys')
    op.drop_index('ix_tokens__api_keys_secret', table_name='tokens__api_keys')
    op.drop_table('tokens__api_keys')
    op.drop_table('clients__clients')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tokens__api_keys',
    sa.Column('secret', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('valid_until', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('client_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['clients__clients.id'], name='tokens__api_keys_client_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='tokens__api_keys_pkey'),
    sa.UniqueConstraint('client_id', 'secret', name='tokens__api_keys_client_id_secret_key')
    )
    op.create_index('ix_tokens__api_keys_secret', 'tokens__api_keys', ['secret'], unique=False)
    op.create_index('ix_tokens__api_keys_is_active', 'tokens__api_keys', ['is_active'], unique=False)
    op.create_index('ix_tokens__api_keys_id', 'tokens__api_keys', ['id'], unique=False)
    op.create_index('ix_tokens__api_keys_client_id', 'tokens__api_keys', ['client_id'], unique=False)
    op.create_table('clients__clients',
    sa.Column('uid', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('authentication_type', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='clients__clients_pkey'),
    sa.UniqueConstraint('name', name='clients__clients_name_key')
    )
    op.create_index('ix_clients__clients_uid', 'clients__clients', ['uid'], unique=True)
    op.create_index('ix_clients__clients_id', 'clients__clients', ['id'], unique=False)
    op.create_table('tokens__access_keys',
    sa.Column('account_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('secret', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('valid_until', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['accounts__client_accounts.id'], name='tokens__access_keys_account_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='tokens__access_keys_pkey'),
    sa.UniqueConstraint('account_id', 'secret', name='tokens__access_keys_account_id_secret_key')
    )
    op.create_index('ix_tokens__access_keys_secret', 'tokens__access_keys', ['secret'], unique=False)
    op.create_index('ix_tokens__access_keys_is_active', 'tokens__access_keys', ['is_active'], unique=False)
    op.create_index('ix_tokens__access_keys_id', 'tokens__access_keys', ['id'], unique=False)
    op.create_index('ix_tokens__access_keys_account_id', 'tokens__access_keys', ['account_id'], unique=False)
    # ### end Alembic commands ###
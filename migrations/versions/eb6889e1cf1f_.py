"""empty message

Revision ID: eb6889e1cf1f
Revises: 3dfcbc1249af
Create Date: 2024-12-01 19:25:34.764098

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'eb6889e1cf1f'
down_revision: Union[str, None] = '3dfcbc1249af'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients__clients',
    sa.Column('uid', sa.String(length=50), nullable=True),
    sa.Column('name', sa.Unicode(length=255), nullable=True),
    sa.Column('authentication_type', sa.Enum('AUTH_TOKEN', 'ACCESS_KEY', name='authenticationtype', native_enum=False), nullable=True),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_clients__clients_id'), 'clients__clients', ['id'], unique=False)
    op.create_index(op.f('ix_clients__clients_uid'), 'clients__clients', ['uid'], unique=True)
    op.drop_index('ix_applications__applications_id', table_name='applications__applications')
    op.drop_index('ix_applications__applications_uid', table_name='applications__applications')
    op.add_column('tokens__api_keys', sa.Column('client_id', sa.UUID(), nullable=False))
    op.drop_index('ix_tokens__api_keys_application_id', table_name='tokens__api_keys')
    op.drop_constraint('tokens__api_keys_application_id_secret_key', 'tokens__api_keys', type_='unique')
    op.create_index(op.f('ix_tokens__api_keys_client_id'), 'tokens__api_keys', ['client_id'], unique=False)
    op.create_unique_constraint(None, 'tokens__api_keys', ['client_id', 'secret'])
    op.drop_constraint('tokens__api_keys_application_id_fkey', 'tokens__api_keys', type_='foreignkey')
    op.create_foreign_key(None, 'tokens__api_keys', 'clients__clients', ['client_id'], ['id'])
    op.drop_column('tokens__api_keys', 'application_id')
    op.drop_table('applications__applications')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tokens__api_keys', sa.Column('application_id', sa.UUID(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'tokens__api_keys', type_='foreignkey')
    op.create_foreign_key('tokens__api_keys_application_id_fkey', 'tokens__api_keys', 'applications__applications', ['application_id'], ['id'])
    op.drop_constraint(None, 'tokens__api_keys', type_='unique')
    op.drop_index(op.f('ix_tokens__api_keys_client_id'), table_name='tokens__api_keys')
    op.create_unique_constraint('tokens__api_keys_application_id_secret_key', 'tokens__api_keys', ['application_id', 'secret'])
    op.create_index('ix_tokens__api_keys_application_id', 'tokens__api_keys', ['application_id'], unique=False)
    op.drop_column('tokens__api_keys', 'client_id')
    op.create_table('applications__applications',
    sa.Column('uid', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('authentication_type', postgresql.ENUM('AUTH_TOKEN', 'ACCESS_KEY', name='applicationauthenticationtype'), autoincrement=False, nullable=True),
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='applications__applications_pkey'),
    sa.UniqueConstraint('name', name='applications__applications_name_key')
    )
    op.create_index('ix_applications__applications_uid', 'applications__applications', ['uid'], unique=True)
    op.create_index('ix_applications__applications_id', 'applications__applications', ['id'], unique=False)
    op.drop_index(op.f('ix_clients__clients_uid'), table_name='clients__clients')
    op.drop_index(op.f('ix_clients__clients_id'), table_name='clients__clients')
    op.drop_table('clients__clients')
    # ### end Alembic commands ###

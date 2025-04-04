"""empty message

Revision ID: 754b0bb0f202
Revises: bbd13678b8fa
Create Date: 2024-12-14 20:24:04.242756

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '754b0bb0f202'
down_revision: Union[str, None] = 'bbd13678b8fa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('search__terminologies',
    sa.Column('uid', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('definition', sa.String(length=2000), nullable=True),
    sa.Column('topics', sa.ARRAY(sa.String(length=50), dimensions=1), nullable=True),
    sa.Column('grammatical_label', sa.String(length=50), nullable=True),
    sa.Column('verified', sa.Boolean(), nullable=False),
    sa.Column('source_name', sa.String(length=255), nullable=True),
    sa.Column('source_url', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_search__terminologies_id'), 'search__terminologies', ['id'], unique=False)
    op.create_index(op.f('ix_search__terminologies_name'), 'search__terminologies', ['name'], unique=False)
    op.create_index(op.f('ix_search__terminologies_uid'), 'search__terminologies', ['uid'], unique=True)
    op.create_table('search__search_records',
    sa.Column('uid', sa.String(length=50), nullable=True),
    sa.Column('query', sa.String(length=255), nullable=True),
    sa.Column('account_id', sa.UUID(), nullable=True),
    sa.Column('made_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['accounts__client_accounts.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_search__search_records_account_id'), 'search__search_records', ['account_id'], unique=False)
    op.create_index(op.f('ix_search__search_records_id'), 'search__search_records', ['id'], unique=False)
    op.create_index(op.f('ix_search__search_records_made_at'), 'search__search_records', ['made_at'], unique=False)
    op.create_index(op.f('ix_search__search_records_query'), 'search__search_records', ['query'], unique=False)
    op.create_index(op.f('ix_search__search_records_uid'), 'search__search_records', ['uid'], unique=True)
    op.drop_index('ix_glossary__terminologies_id', table_name='glossary__terminologies')
    op.drop_index('ix_glossary__terminologies_name', table_name='glossary__terminologies')
    op.drop_index('ix_glossary__terminologies_uid', table_name='glossary__terminologies')
    op.drop_table('glossary__terminologies')
    op.drop_constraint('clients__api_clients_account_id_fkey', 'clients__api_clients', type_='foreignkey')
    op.create_foreign_key(None, 'clients__api_clients', 'accounts__client_accounts', ['account_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('clients__api_keys_client_id_fkey', 'clients__api_keys', type_='foreignkey')
    op.create_foreign_key(None, 'clients__api_keys', 'clients__api_clients', ['client_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'clients__api_keys', type_='foreignkey')
    op.create_foreign_key('clients__api_keys_client_id_fkey', 'clients__api_keys', 'clients__api_clients', ['client_id'], ['id'])
    op.drop_constraint(None, 'clients__api_clients', type_='foreignkey')
    op.create_foreign_key('clients__api_clients_account_id_fkey', 'clients__api_clients', 'accounts__client_accounts', ['account_id'], ['id'])
    op.create_table('glossary__terminologies',
    sa.Column('uid', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('definition', sa.VARCHAR(length=2000), autoincrement=False, nullable=True),
    sa.Column('topics', postgresql.ARRAY(sa.VARCHAR(length=50)), autoincrement=False, nullable=True),
    sa.Column('grammatical_label', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('verified', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('source_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('source_url', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='glossary__terminologies_pkey')
    )
    op.create_index('ix_glossary__terminologies_uid', 'glossary__terminologies', ['uid'], unique=True)
    op.create_index('ix_glossary__terminologies_name', 'glossary__terminologies', ['name'], unique=False)
    op.create_index('ix_glossary__terminologies_id', 'glossary__terminologies', ['id'], unique=False)
    op.drop_index(op.f('ix_search__search_records_uid'), table_name='search__search_records')
    op.drop_index(op.f('ix_search__search_records_query'), table_name='search__search_records')
    op.drop_index(op.f('ix_search__search_records_made_at'), table_name='search__search_records')
    op.drop_index(op.f('ix_search__search_records_id'), table_name='search__search_records')
    op.drop_index(op.f('ix_search__search_records_account_id'), table_name='search__search_records')
    op.drop_table('search__search_records')
    op.drop_index(op.f('ix_search__terminologies_uid'), table_name='search__terminologies')
    op.drop_index(op.f('ix_search__terminologies_name'), table_name='search__terminologies')
    op.drop_index(op.f('ix_search__terminologies_id'), table_name='search__terminologies')
    op.drop_table('search__terminologies')
    # ### end Alembic commands ###

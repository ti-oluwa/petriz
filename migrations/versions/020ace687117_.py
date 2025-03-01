"""empty message

Revision ID: 020ace687117
Revises: 6959f08a108e
Create Date: 2025-02-20 21:01:43.930344

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '020ace687117'
down_revision: Union[str, None] = '6959f08a108e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('search__terms', sa.Column('search_tsvector', postgresql.TSVECTOR(), nullable=True))
    op.drop_index('ix_search__terms_definition_tsvector', table_name='search__terms')
    op.drop_index('ix_terms_definition_tsvector', table_name='search__terms', postgresql_using='gin')
    op.create_index(op.f('ix_search__terms_search_tsvector'), 'search__terms', ['search_tsvector'], unique=False)
    op.create_index('ix_terms_search_tsvector', 'search__terms', ['search_tsvector'], unique=False, postgresql_using='gin')
    op.drop_column('search__terms', 'definition_tsvector')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('search__terms', sa.Column('definition_tsvector', postgresql.TSVECTOR(), autoincrement=False, nullable=True))
    op.drop_index('ix_terms_search_tsvector', table_name='search__terms', postgresql_using='gin')
    op.drop_index(op.f('ix_search__terms_search_tsvector'), table_name='search__terms')
    op.create_index('ix_terms_definition_tsvector', 'search__terms', ['definition_tsvector'], unique=False, postgresql_using='gin')
    op.create_index('ix_search__terms_definition_tsvector', 'search__terms', ['definition_tsvector'], unique=False)
    op.drop_column('search__terms', 'search_tsvector')
    # ### end Alembic commands ###

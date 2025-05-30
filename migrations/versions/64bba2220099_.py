"""empty message

Revision ID: 64bba2220099
Revises: ea5bc8f32481
Create Date: 2025-02-16 01:56:23.621855

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '64bba2220099'
down_revision: Union[str, None] = 'ea5bc8f32481'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('search__search_records', 'topics')
    op.drop_index('ix_search__terms_views', table_name='search__terms')
    op.drop_column('search__terms', 'topics')
    op.drop_column('search__terms', 'views')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('search__terms', sa.Column('views', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('search__terms', sa.Column('topics', postgresql.ARRAY(sa.VARCHAR(length=50)), autoincrement=False, nullable=True))
    op.create_index('ix_search__terms_views', 'search__terms', ['views'], unique=False)
    op.add_column('search__search_records', sa.Column('topics', postgresql.ARRAY(sa.VARCHAR(length=50)), autoincrement=False, nullable=True))
    # ### end Alembic commands ###

"""empty message

Revision ID: e83f05dfc9a7
Revises: 9ea8f5fd9599
Create Date: 2025-03-03 00:39:57.104645

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e83f05dfc9a7'
down_revision: Union[str, None] = '9ea8f5fd9599'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('audits__audit_log_entries', 'actor_id',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('audits__audit_log_entries', 'actor_type',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('audits__audit_log_entries', 'actor_type',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('audits__audit_log_entries', 'actor_id',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###

"""Added TOTP models

Revision ID: 8b35237eb257
Revises: 93af4ee90d80
Create Date: 2024-11-23 12:22:30.035742

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b35237eb257'
down_revision: Union[str, None] = '93af4ee90d80'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accounts__client_access_keys', sa.Column('secret', sa.String(length=50), nullable=True))
    op.add_column('accounts__client_access_keys', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.drop_index('ix_accounts__client_access_keys_key', table_name='accounts__client_access_keys')
    op.create_index(op.f('ix_accounts__client_access_keys_secret'), 'accounts__client_access_keys', ['secret'], unique=False)
    op.create_unique_constraint(None, 'accounts__client_access_keys', ['account_id', 'secret'])
    op.drop_column('accounts__client_access_keys', 'key')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accounts__client_access_keys', sa.Column('key', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'accounts__client_access_keys', type_='unique')
    op.drop_index(op.f('ix_accounts__client_access_keys_secret'), table_name='accounts__client_access_keys')
    op.create_index('ix_accounts__client_access_keys_key', 'accounts__client_access_keys', ['key'], unique=False)
    op.drop_column('accounts__client_access_keys', 'created_at')
    op.drop_column('accounts__client_access_keys', 'secret')
    # ### end Alembic commands ###

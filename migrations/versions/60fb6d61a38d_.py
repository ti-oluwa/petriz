"""empty message

Revision ID: 60fb6d61a38d
Revises: 0fd91c6fb4ca
Create Date: 2024-12-06 21:35:06.057879

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60fb6d61a38d'
down_revision: Union[str, None] = '0fd91c6fb4ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clients__api_keys', sa.Column('uid', sa.String(length=50), nullable=True))
    op.create_index(op.f('ix_clients__api_keys_uid'), 'clients__api_keys', ['uid'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_clients__api_keys_uid'), table_name='clients__api_keys')
    op.drop_column('clients__api_keys', 'uid')
    # ### end Alembic commands ###

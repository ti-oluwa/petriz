"""Added TOTP models

Revision ID: 2d518f59d3c3
Revises: 8b35237eb257
Create Date: 2024-11-23 13:31:59.218495

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision: str = "2d518f59d3c3"
down_revision: Union[str, None] = "8b35237eb257"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tokens__identifier_related_totps",
        sa.Column("identifier", sa.String(length=255), nullable=False),
        sa.Column("key", sa.String(length=100), nullable=False),
        sa.Column("last_verified_counter", sa.Integer(), nullable=False),
        sa.Column("validity_period", sa.Integer(), nullable=False),
        sa.Column("length", sa.Integer(), nullable=False),
        sa.Column(
            "requestor_ip_address",
            sqlalchemy_utils.types.ip_address.IPAddressType(length=50),
            nullable=True,
        ),
        sa.Column("extradata", sa.JSON(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("key"),
    )
    op.create_index(
        op.f("ix_tokens__identifier_related_totps_id"),
        "tokens__identifier_related_totps",
        ["id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_tokens__identifier_related_totps_identifier"),
        "tokens__identifier_related_totps",
        ["identifier"],
        unique=False,
    )
    op.create_table(
        "tokens__account_related_totps",
        sa.Column("account_id", sa.UUID(), nullable=False),
        sa.Column("key", sa.String(length=100), nullable=False),
        sa.Column("last_verified_counter", sa.Integer(), nullable=False),
        sa.Column("validity_period", sa.Integer(), nullable=False),
        sa.Column("length", sa.Integer(), nullable=False),
        sa.Column(
            "requestor_ip_address",
            sqlalchemy_utils.types.ip_address.IPAddressType(length=50),
            nullable=True,
        ),
        sa.Column("extradata", sa.JSON(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["account_id"],
            ["accounts__client_accounts.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("key"),
    )
    op.create_index(
        op.f("ix_tokens__account_related_totps_account_id"),
        "tokens__account_related_totps",
        ["account_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_tokens__account_related_totps_id"),
        "tokens__account_related_totps",
        ["id"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_tokens__account_related_totps_id"),
        table_name="tokens__account_related_totps",
    )
    op.drop_index(
        op.f("ix_tokens__account_related_totps_account_id"),
        table_name="tokens__account_related_totps",
    )
    op.drop_table("tokens__account_related_totps")
    op.drop_index(
        op.f("ix_tokens__identifier_related_totps_identifier"),
        table_name="tokens__identifier_related_totps",
    )
    op.drop_index(
        op.f("ix_tokens__identifier_related_totps_id"),
        table_name="tokens__identifier_related_totps",
    )
    op.drop_table("tokens__identifier_related_totps")
    # ### end Alembic commands ###

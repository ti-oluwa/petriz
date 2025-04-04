"""empty message

Revision ID: 4dea7c9fed8f
Revises: 9b882aeed913
Create Date: 2024-12-23 01:16:46.953990

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision: str = "4dea7c9fed8f"
down_revision: Union[str, None] = "9b882aeed913"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        "ix_tokens__connection_identifier_related_totps_id",
        table_name="tokens__connection_identifier_related_totps",
    )
    op.drop_index(
        "ix_tokens__connection_identifier_related_totps_identifier",
        table_name="tokens__connection_identifier_related_totps",
    )
    op.drop_table("tokens__connection_identifier_related_totps")
    op.alter_column(
        "accounts__client_accounts",
        "uid",
        existing_type=sa.VARCHAR(length=50),
        nullable=False,
    )
    op.alter_column(
        "accounts__client_accounts",
        "name",
        existing_type=sa.VARCHAR(length=50),
        nullable=False,
    )
    op.alter_column(
        "accounts__client_accounts",
        "is_active",
        existing_type=sa.BOOLEAN(),
        nullable=False,
    )
    op.alter_column(
        "accounts__client_accounts",
        "is_staff",
        existing_type=sa.BOOLEAN(),
        nullable=False,
    )
    op.alter_column(
        "accounts__client_accounts",
        "is_admin",
        existing_type=sa.BOOLEAN(),
        nullable=False,
    )
    op.create_unique_constraint(None, "accounts__client_accounts", ["name"])
    op.alter_column(
        "clients__api_clients",
        "uid",
        existing_type=sa.VARCHAR(length=50),
        nullable=False,
    )
    op.alter_column(
        "clients__api_clients",
        "name",
        existing_type=sa.VARCHAR(length=50),
        nullable=False,
    )
    op.alter_column(
        "clients__api_clients", "disabled", existing_type=sa.BOOLEAN(), nullable=False
    )
    op.alter_column(
        "clients__api_keys", "uid", existing_type=sa.VARCHAR(length=50), nullable=False
    )
    op.drop_index("ix_clients__api_keys_client_id", table_name="clients__api_keys")
    op.create_index(
        op.f("ix_clients__api_keys_client_id"),
        "clients__api_keys",
        ["client_id"],
        unique=True,
    )
    op.alter_column(
        "search__account_search_metrics",
        "uid",
        existing_type=sa.VARCHAR(length=50),
        nullable=False,
    )
    op.alter_column(
        "search__account_search_metrics",
        "search_count",
        existing_type=sa.INTEGER(),
        nullable=False,
    )
    op.alter_column(
        "search__glossary_metrics",
        "term_count",
        existing_type=sa.INTEGER(),
        nullable=False,
    )
    op.alter_column(
        "search__glossary_metrics",
        "search_count",
        existing_type=sa.INTEGER(),
        nullable=False,
    )
    op.alter_column(
        "search__glossary_metrics",
        "verified_term_count",
        existing_type=sa.INTEGER(),
        nullable=False,
    )
    op.alter_column(
        "search__glossary_metrics",
        "unverified_term_count",
        existing_type=sa.INTEGER(),
        nullable=False,
    )
    op.alter_column(
        "search__search_records",
        "uid",
        existing_type=sa.VARCHAR(length=50),
        nullable=False,
    )
    op.alter_column(
        "search__search_records",
        "timestamp",
        existing_type=postgresql.TIMESTAMP(timezone=True),
        nullable=False,
    )
    op.add_column(
        "search__terms",
        sa.Column("views", sa.Integer(), nullable=True, insert_default=0),
    )
    op.alter_column(
        "search__terms", "uid", existing_type=sa.VARCHAR(length=50), nullable=False
    )
    op.alter_column(
        "search__terms", "name", existing_type=sa.VARCHAR(length=255), nullable=False
    )
    op.alter_column(
        "search__terms",
        "definition",
        existing_type=sa.VARCHAR(length=5000),
        nullable=False,
    )
    op.create_index(
        op.f("ix_search__terms_source_name"),
        "search__terms",
        ["source_name"],
        unique=False,
    )
    op.create_index(
        op.f("ix_search__terms_views"), "search__terms", ["views"], unique=False
    )
    op.drop_constraint(
        "tokens__account_related_totps_account_id_fkey",
        "tokens__account_related_totps",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "tokens__account_related_totps",
        "accounts__client_accounts",
        ["account_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.alter_column(
        "tokens__auth_tokens", "is_active", existing_type=sa.BOOLEAN(), nullable=False
    )
    op.create_index(
        op.f("ix_tokens__auth_tokens_valid_until"),
        "tokens__auth_tokens",
        ["valid_until"],
        unique=False,
    )
    op.drop_constraint(
        "tokens__auth_tokens_account_id_fkey", "tokens__auth_tokens", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "tokens__auth_tokens",
        "accounts__client_accounts",
        ["account_id"],
        ["id"],
        ondelete="CASCADE",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "tokens__auth_tokens", type_="foreignkey")
    op.create_foreign_key(
        "tokens__auth_tokens_account_id_fkey",
        "tokens__auth_tokens",
        "accounts__client_accounts",
        ["account_id"],
        ["id"],
    )
    op.drop_index(
        op.f("ix_tokens__auth_tokens_valid_until"), table_name="tokens__auth_tokens"
    )
    op.alter_column(
        "tokens__auth_tokens", "is_active", existing_type=sa.BOOLEAN(), nullable=True
    )
    op.drop_constraint(None, "tokens__account_related_totps", type_="foreignkey")
    op.create_foreign_key(
        "tokens__account_related_totps_account_id_fkey",
        "tokens__account_related_totps",
        "accounts__client_accounts",
        ["account_id"],
        ["id"],
    )
    op.drop_index(op.f("ix_search__terms_views"), table_name="search__terms")
    op.drop_index(op.f("ix_search__terms_source_name"), table_name="search__terms")
    op.alter_column(
        "search__terms",
        "source_url",
        existing_type=sqlalchemy_utils.types.url.URLType(length=255),
        type_=sa.VARCHAR(length=255),
        existing_nullable=True,
    )
    op.alter_column(
        "search__terms",
        "definition",
        existing_type=sa.VARCHAR(length=5000),
        nullable=True,
    )
    op.alter_column(
        "search__terms", "name", existing_type=sa.VARCHAR(length=255), nullable=True
    )
    op.alter_column(
        "search__terms", "uid", existing_type=sa.VARCHAR(length=50), nullable=True
    )
    op.drop_column("search__terms", "views")
    op.alter_column(
        "search__search_records",
        "timestamp",
        existing_type=postgresql.TIMESTAMP(timezone=True),
        nullable=True,
    )
    op.alter_column(
        "search__search_records",
        "uid",
        existing_type=sa.VARCHAR(length=50),
        nullable=True,
    )
    op.alter_column(
        "search__glossary_metrics",
        "unverified_term_count",
        existing_type=sa.INTEGER(),
        nullable=True,
    )
    op.alter_column(
        "search__glossary_metrics",
        "verified_term_count",
        existing_type=sa.INTEGER(),
        nullable=True,
    )
    op.alter_column(
        "search__glossary_metrics",
        "search_count",
        existing_type=sa.INTEGER(),
        nullable=True,
    )
    op.alter_column(
        "search__glossary_metrics",
        "term_count",
        existing_type=sa.INTEGER(),
        nullable=True,
    )
    op.alter_column(
        "search__account_search_metrics",
        "search_count",
        existing_type=sa.INTEGER(),
        nullable=True,
    )
    op.alter_column(
        "search__account_search_metrics",
        "uid",
        existing_type=sa.VARCHAR(length=50),
        nullable=True,
    )
    op.drop_index(
        op.f("ix_clients__api_keys_client_id"), table_name="clients__api_keys"
    )
    op.create_index(
        "ix_clients__api_keys_client_id",
        "clients__api_keys",
        ["client_id"],
        unique=False,
    )
    op.alter_column(
        "clients__api_keys", "uid", existing_type=sa.VARCHAR(length=50), nullable=True
    )
    op.alter_column(
        "clients__api_clients", "disabled", existing_type=sa.BOOLEAN(), nullable=True
    )
    op.alter_column(
        "clients__api_clients",
        "name",
        existing_type=sa.VARCHAR(length=50),
        nullable=True,
    )
    op.alter_column(
        "clients__api_clients",
        "uid",
        existing_type=sa.VARCHAR(length=50),
        nullable=True,
    )
    op.drop_constraint(None, "accounts__client_accounts", type_="unique")
    op.alter_column(
        "accounts__client_accounts",
        "is_admin",
        existing_type=sa.BOOLEAN(),
        nullable=True,
    )
    op.alter_column(
        "accounts__client_accounts",
        "is_staff",
        existing_type=sa.BOOLEAN(),
        nullable=True,
    )
    op.alter_column(
        "accounts__client_accounts",
        "is_active",
        existing_type=sa.BOOLEAN(),
        nullable=True,
    )
    op.alter_column(
        "accounts__client_accounts",
        "name",
        existing_type=sa.VARCHAR(length=50),
        nullable=True,
    )
    op.alter_column(
        "accounts__client_accounts",
        "uid",
        existing_type=sa.VARCHAR(length=50),
        nullable=True,
    )
    op.create_table(
        "tokens__connection_identifier_related_totps",
        sa.Column(
            "identifier", sa.VARCHAR(length=255), autoincrement=False, nullable=False
        ),
        sa.Column("key", sa.VARCHAR(length=100), autoincrement=False, nullable=False),
        sa.Column(
            "last_verified_counter", sa.INTEGER(), autoincrement=False, nullable=False
        ),
        sa.Column("validity_period", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("length", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column(
            "requestor_ip_address",
            sa.VARCHAR(length=50),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "extradata",
            postgresql.JSON(astext_type=sa.Text()),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint(
            "id", name="tokens__connection_identifier_related_totps_pkey"
        ),
        sa.UniqueConstraint(
            "key", name="tokens__connection_identifier_related_totps_key_key"
        ),
    )
    op.create_index(
        "ix_tokens__connection_identifier_related_totps_identifier",
        "tokens__connection_identifier_related_totps",
        ["identifier"],
        unique=False,
    )
    op.create_index(
        "ix_tokens__connection_identifier_related_totps_id",
        "tokens__connection_identifier_related_totps",
        ["id"],
        unique=False,
    )
    # ### end Alembic commands ###

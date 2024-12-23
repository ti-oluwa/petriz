import datetime
import faker
import typing
import fastapi.exceptions
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from .models import (
    APIClient,
    APIKey,
    generate_api_client_uid,
    generate_api_key_secret,
    generate_api_key_uid,
)
from apps.accounts.models import Account

fake = faker.Faker("en-us")


###############
# API CLIENTS #
###############


def generate_api_client_name() -> str:
    words = fake.words(nb=6, unique=True)
    return "-".join(words[:4])


async def check_api_client_name_exists_for_account(
    session: AsyncSession, account_id: str, name: str
) -> bool:
    """Check if a client name exists for an account."""
    exists = await session.execute(
        sa.select(
            sa.exists().where(
                sa.and_(APIClient.name == name, APIClient.account_id == account_id)
            )
        )
    )
    return exists.scalar()


async def check_account_can_create_more_clients(
    session: AsyncSession, account: Account
):
    client_count = await session.execute(
        sa.select(sa.func.count()).where(APIClient.account_id == account.id)
    )
    return client_count.scalar() < Account.MAX_CLIENT_COUNT


async def create_api_client(
    session: AsyncSession,
    account_id: typing.Optional[str] = None,
    name: typing.Optional[str] = None,
    **kwargs,
):
    if name and account_id:
        if await check_api_client_name_exists_for_account(session, account_id, name):
            raise fastapi.exceptions.ValidationException(
                errors=[
                    "Client with this name already exists for account.",
                ]
            )

    while True:
        uid = generate_api_client_uid()
        if not name:
            name = generate_api_client_name()

        query_clause = sa.or_(APIClient.uid == uid, APIClient.name == name)
        if account_id:
            query_clause = sa.or_(
                APIClient.uid == uid,
                sa.and_(APIClient.name == name, APIClient.account_id == account_id),
            )

        exists = await session.execute(sa.select(sa.exists().where(query_clause)))
        if not exists.scalar():
            break

    if account_id:
        kwargs["client_type"] = APIClient.ClientType.USER

    api_client = APIClient(
        uid=uid,
        name=name,
        account_id=account_id,
        **kwargs,
    )
    session.add(api_client)
    return api_client


async def retrieve_api_client(
    session: AsyncSession, **filters
) -> typing.Optional[APIClient]:
    """
    Retrieve the first API client that matches the given filter from the DB.
    Eagerly load the associated api key and account (if any).
    """
    result = await session.execute(
        sa.select(APIClient)
        .filter_by(**filters)
        .options(joinedload(APIClient.api_key), joinedload(APIClient.account))
    )
    return result.scalar_one_or_none()


async def retrieve_api_clients(
    session: AsyncSession,
    *,
    limit: int = 100,
    offset: int = 0,
    **filters,
):
    result = await session.execute(
        sa.select(APIClient)
        .filter_by(**filters)
        .limit(limit)
        .offset(offset)
        .options(joinedload(APIClient.api_key), joinedload(APIClient.account))
    )
    return result.scalars().all()


async def retrieve_api_clients_by_uid(
    session: AsyncSession, uids: typing.List[str], **filters
):
    result = await session.execute(
        sa.select(APIClient).where(APIClient.id.in_(uids)).filter_by(**filters)
    )
    return result.scalars().all()


async def delete_api_clients_by_uid(session: AsyncSession, uids: typing.List[str], **filters):
    result = await session.execute(
        sa.delete(APIClient).where(APIClient.id.in_(uids)).filter_by(**filters)
    )
    return result.scalar()


############
# API KEYS #
############


async def check_api_key_for_client_exists(
    session: AsyncSession, client: APIClient
) -> bool:
    """Check if an api key exists for a client."""
    exists = await session.execute(
        sa.select(sa.exists().where(APIKey.client_id == client.id))
    )
    return exists


async def create_api_key(
    session: AsyncSession,
    client: APIClient,
    valid_until: typing.Optional[datetime.datetime] = None,
) -> APIKey:
    """Create a new api key for the API client."""
    while True:
        uid = generate_api_key_uid()
        secret = generate_api_key_secret()
        exists = await session.execute(
            sa.select(
                sa.exists().where(sa.or_(APIKey.uid == uid, APIKey.secret == secret))
            )
        )
        if not exists.scalar():
            break

    api_key = APIKey(
        uid=uid,
        secret=secret,
        client_id=client.id,
        valid_until=valid_until,
    )
    session.add(api_key)
    return api_key


async def retrieve_api_key_by_secret(
    session: AsyncSession, secret: str
) -> typing.Optional[APIKey]:
    """Retrieve an api key by its secret. Eagerly load the associated client."""
    result = await session.execute(
        sa.select(APIKey)
        .where(APIKey.secret == secret)
        .options(joinedload(APIKey.client))
    )
    return result.scalar_one_or_none()


async def refresh_api_key_secret(session: AsyncSession, api_key: APIKey):
    api_key.secret = generate_api_key_secret()
    session.add(api_key)
    return api_key


__all__ = [
    "create_api_client",
    "retrieve_api_client",
    "retrieve_api_clients",
    "check_api_key_for_client_exists",
    "create_api_key",
    "retrieve_api_key_by_secret",
]

from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa
from sqlalchemy.orm import joinedload

from apps.accounts.models import Account
from .models import AuthToken, generate_auth_token_secret


async def check_auth_token_for_account_exists(
    session: AsyncSession, account: Account
) -> bool:
    """Check if an auth token exists for the account."""
    exists = await session.execute(
        sa.select(sa.exists().where(AuthToken.account_id == account.id))
    )
    return exists.scalar()


async def create_auth_token(session: AsyncSession, account: Account) -> AuthToken:
    """Create a new auth token for an account."""
    while True:
        secret = generate_auth_token_secret()
        exists = await session.execute(
            sa.select(sa.exists().where(AuthToken.secret == secret))
        )
        if not exists.scalar():
            break

    auth_token = AuthToken(secret=secret, account_id=account.id)
    session.add(auth_token)
    return auth_token


async def get_or_create_auth_token(session: AsyncSession, account: Account):
    result = await session.execute(
        sa.select(AuthToken).where(AuthToken.account_id == account.id)
    )
    
    created = False
    existing_token = result.scalar()
    if not existing_token:
        new_token = await create_auth_token(session=session, account=account)
        created = True
        return new_token, created
    return existing_token, created


async def get_auth_token_by_secret(
    session: AsyncSession, secret: str
) -> AuthToken:
    """Get an auth token by its secret."""
    result = await session.execute(
        sa.select(AuthToken)
        .where(AuthToken.secret == secret)
        .options(joinedload(AuthToken.owner))
    )
    return result.scalar_one_or_none()

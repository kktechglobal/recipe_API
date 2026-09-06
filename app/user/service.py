from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.security import hash_password, verify_password
from app.user.models import User
from app.user.schemas import UserCreate


async def create_user(
    session: AsyncSession,
    user_data: UserCreate,
) -> User:
    """Create and save a new user."""

    username_result = await session.execute(
        select(User).where(
            User.username == user_data.username
        )
    )

    existing_username = username_result.scalar_one_or_none()

    if existing_username:
        raise ValueError("Username already exists")

    email_result = await session.execute(
        select(User).where(
            User.email == user_data.email
        )
    )

    existing_email = email_result.scalar_one_or_none()

    if existing_email:
        raise ValueError("Email already exists")

    user = User(
        username=user_data.username,
        email=user_data.email,
        password=hash_password(user_data.password),
    )

    session.add(user)

    await session.commit()
    await session.refresh(user)

    return user


async def authenticate_user(
    session: AsyncSession,
    email: str,
    password: str,
) -> User | None:

    result = await session.execute(
        select(User).where(User.email == email)
    )

    user = result.scalar_one_or_none()

    if user is None:
        return None

    if not verify_password(
        password,
        user.password,
    ):
        return None

    return user
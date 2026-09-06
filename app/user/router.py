from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import get_current_user
from app.auth.security import create_access_token
from app.database.db import get_session
from app.user.models import User
from app.user.schemas import (
    TokenResponse,
    UserCreate,
    UserLogin,
    UserResponse,
)
from app.user.service import authenticate_user, create_user


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register_user(
    user_data: UserCreate,
    session: AsyncSession = Depends(get_session),
):
    try:
        user = await create_user(session, user_data)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error

    return user


@router.post(
    "/login",
    response_model=TokenResponse,
)
async def login_user(
    user_data: UserLogin,
    session: AsyncSession = Depends(get_session),
):
    user = await authenticate_user(
        session,
        user_data.email,
        user_data.password,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(user.id)

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


@router.get(
    "/me",
    response_model=UserResponse,
)
async def get_my_profile(
    current_user: User = Depends(get_current_user),
):
    return current_user




# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.ext.asyncio import AsyncSession

# from app.auth.security import create_access_token
# from app.database.db import get_session
# from app.user.schemas import TokenResponse, UserCreate, UserLogin, UserResponse
# from app.user.service import authenticate_user, create_user


# router = APIRouter(prefix="/users", tags=["Users"])




# # @router.get(
# #     "/me",
# #     response_model=UserResponse,
# # )
# # async def get_my_profile(
# #     current_user: User = Depends(get_current_user),
# # ):
# #     return current_user




# @router.post(
#     "/",
#     response_model=UserResponse,
#     status_code=status.HTTP_201_CREATED,
# )
# async def register_user(
#     user_data: UserCreate,
#     session: AsyncSession = Depends(get_session),
# ):
#     try:
#         user = await create_user(session, user_data)
#     except ValueError as error:
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT,
#             detail=str(error),
#         ) from error

#     return user


# @router.post(
#     "/login",
#     response_model=TokenResponse,
# )
# async def login_user(
#     user_data: UserLogin,
#     session: AsyncSession = Depends(get_session),
# ):
#     user = await authenticate_user(
#         session,
#         user_data.email,
#         user_data.password,
#     )

#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid email or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

#     access_token = create_access_token(user.id)

#     return {
#         "access_token": access_token,
#         "token_type": "bearer",
#     }






# # from fastapi import APIRouter, Depends, HTTPException, status
# # from sqlalchemy.ext.asyncio import AsyncSession

# # from app.user.schemas import UserCreate, UserResponse
# # from app.user.service import create_user
# # from app.database.db import get_session


# # router = APIRouter(
# #     prefix="/users",
# #     tags=["Users"],
# # )


# # @router.post(
# #     "/",
# #     response_model=UserResponse,
# #     status_code=status.HTTP_201_CREATED,
# # )
# # async def register_user(
# #     user_data: UserCreate,
# #     session: AsyncSession = Depends(get_session),
# # ):
# #     """Create a new user."""

# #     try:
# #         user = await create_user(session, user_data)

# #     except ValueError as error:
# #         raise HTTPException(
# #             status_code=status.HTTP_409_CONFLICT,
# #             detail=str(error),
# #         ) from error

# #     return user
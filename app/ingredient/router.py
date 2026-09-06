from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import get_current_user
from app.database.db import get_session
from app.ingredient.service import IngredientService
from app.user.models import User


router = APIRouter(
    prefix="/ingredients",
    tags=["Ingredients"],
)

service = IngredientService()


class IngredientCreate(BaseModel):
    name: str
    retrieve: str | None = None


class IngredientUpdate(BaseModel):
    name: str | None = None
    retrieve: str | None = None


# =========================
# CREATE
# =========================

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create_ingredient(
    ingredient_data: IngredientCreate,
    db: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    return await service.create_ingredient(
        db,
        ingredient_data.name,
        ingredient_data.retrieve,
    )


# =========================
# GET ALL
# =========================

@router.get("/")
async def get_ingredients(
    db: AsyncSession = Depends(get_session),
):
    return await service.get_ingredients(db)


# =========================
# GET ONE
# =========================

@router.get("/{ingredient_id}")
async def get_ingredient(
    ingredient_id: int,
    db: AsyncSession = Depends(get_session),
):
    ingredient = await service.get_ingredient(
        db,
        ingredient_id,
    )

    if ingredient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ingredient not found",
        )

    return ingredient


# =========================
# UPDATE
# =========================

@router.put("/{ingredient_id}")
async def update_ingredient(
    ingredient_id: int,
    ingredient_data: IngredientUpdate,
    db: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    ingredient = await service.update_ingredient(
        db,
        ingredient_id,
        ingredient_data.name,
        ingredient_data.retrieve,
    )

    if ingredient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ingredient not found",
        )

    return ingredient


# =========================
# DELETE
# =========================

@router.delete(
    "/{ingredient_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_ingredient(
    ingredient_id: int,
    db: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    deleted = await service.delete_ingredient(
        db,
        ingredient_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ingredient not found",
        )

    return None










# from fastapi import APIRouter, Depends, HTTPException, status
# from pydantic import BaseModel
# from sqlalchemy.ext.asyncio import AsyncSession

# from app.database.db import get_session
# from app.ingredient.service import IngredientService


# router = APIRouter(
#     prefix="/ingredients",
#     tags=["Ingredients"]
# )

# service = IngredientService()


# class IngredientCreate(BaseModel):
#     name: str
#     retrieve: str | None = None


# class IngredientUpdate(BaseModel):
#     name: str | None = None
#     retrieve: str | None = None


# @router.post(
#     "/",
#     status_code=status.HTTP_201_CREATED
# )
# async def create_ingredient(
#     ingredient_data: IngredientCreate,
#     db: AsyncSession = Depends(get_session),
# ):
#     return await service.create_ingredient(
#         db,
#         ingredient_data.name,
#         ingredient_data.retrieve,
#     )


# @router.get("/")
# async def get_ingredients(
#     db: AsyncSession = Depends(get_session),
# ):
#     return await service.get_ingredients(db)


# @router.get("/{ingredient_id}")
# async def get_ingredient(
#     ingredient_id: int,
#     db: AsyncSession = Depends(get_session),
# ):
#     ingredient = await service.get_ingredient(
#         db,
#         ingredient_id
#     )

#     if ingredient is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Ingredient not found",
#         )

#     return ingredient


# @router.put("/{ingredient_id}")
# async def update_ingredient(
#     ingredient_id: int,
#     ingredient_data: IngredientUpdate,
#     db: AsyncSession = Depends(get_session),
# ):
#     ingredient = await service.update_ingredient(
#         db,
#         ingredient_id,
#         ingredient_data.name,
#         ingredient_data.retrieve,
#     )

#     if ingredient is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Ingredient not found",
#         )

#     return ingredient


# @router.delete(
#     "/{ingredient_id}",
#     status_code=status.HTTP_204_NO_CONTENT
# )
# async def delete_ingredient(
#     ingredient_id: int,
#     db: AsyncSession = Depends(get_session),
# ):
#     deleted = await service.delete_ingredient(
#         db,
#         ingredient_id
#     )

#     if not deleted:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Ingredient not found",
#         )

#     return None
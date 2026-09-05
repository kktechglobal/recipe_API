from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.db import get_session
from app.RecipeIngredient.service import RecipeIngredientService


router = APIRouter(
    prefix="/recipes",
    tags=["Recipe Ingredients"]
)

service = RecipeIngredientService()


class RecipeIngredientCreate(BaseModel):
    ingredient_id: int
    amount: float | None = None
    unit: str
    preparation: str | None = None


class RecipeIngredientUpdate(BaseModel):
    amount: float | None = None
    unit: str | None = None
    preparation: str | None = None


@router.post(
    "/{recipe_id}/ingredients",
    status_code=status.HTTP_201_CREATED
)
async def create_recipe_ingredient(
    recipe_id: int,
    ingredient_data: RecipeIngredientCreate,
    db: AsyncSession = Depends(get_session),
):
    return await service.create_recipe_ingredient(
        db,
        recipe_id,
        ingredient_data.ingredient_id,
        ingredient_data.amount,
        ingredient_data.unit,
        ingredient_data.preparation,
    )


@router.get("/{recipe_id}/ingredients")
async def get_recipe_ingredients(
    recipe_id: int,
    db: AsyncSession = Depends(get_session),
):
    return await service.get_recipe_ingredients(
        db,
        recipe_id
    )


@router.get("/ingredients/{recipe_ingredient_id}")
async def get_recipe_ingredient(
    recipe_ingredient_id: int,
    db: AsyncSession = Depends(get_session),
):
    item = await service.get_recipe_ingredient(
        db,
        recipe_ingredient_id
    )

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe ingredient not found",
        )

    return item


@router.put("/ingredients/{recipe_ingredient_id}")
async def update_recipe_ingredient(
    recipe_ingredient_id: int,
    ingredient_data: RecipeIngredientUpdate,
    db: AsyncSession = Depends(get_session),
):
    item = await service.update_recipe_ingredient(
        db,
        recipe_ingredient_id,
        ingredient_data.amount,
        ingredient_data.unit,
        ingredient_data.preparation,
    )

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe ingredient not found",
        )

    return item


@router.delete(
    "/ingredients/{recipe_ingredient_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_recipe_ingredient(
    recipe_ingredient_id: int,
    db: AsyncSession = Depends(get_session),
):
    deleted = await service.delete_recipe_ingredient(
        db,
        recipe_ingredient_id
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe ingredient not found",
        )

    return None
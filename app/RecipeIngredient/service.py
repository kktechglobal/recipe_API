from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.RecipeIngredient.models import RecipeIngredient


class RecipeIngredientService:

    async def create_recipe_ingredient(
        self,
        db: AsyncSession,
        recipe_id: int,
        ingredient_id: int,
        amount: float | None,
        unit: str,
        preparation: str | None = None,
    ) -> RecipeIngredient:

        recipe_ingredient = RecipeIngredient(
            recipe_id=recipe_id,
            ingredient_id=ingredient_id,
            amount=amount,
            unit=unit,
            preparation=preparation,
        )

        db.add(recipe_ingredient)
        await db.commit()
        await db.refresh(recipe_ingredient)

        return recipe_ingredient

    async def get_recipe_ingredients(
        self,
        db: AsyncSession,
        recipe_id: int,
    ) -> list[RecipeIngredient]:

        result = await db.execute(
            select(RecipeIngredient)
            .where(RecipeIngredient.recipe_id == recipe_id)
        )

        return list(result.scalars().all())

    async def get_recipe_ingredient(
        self,
        db: AsyncSession,
        recipe_ingredient_id: int,
    ) -> RecipeIngredient | None:

        result = await db.execute(
            select(RecipeIngredient)
            .where(
                RecipeIngredient.id == recipe_ingredient_id
            )
        )

        return result.scalar_one_or_none()

    async def update_recipe_ingredient(
        self,
        db: AsyncSession,
        recipe_ingredient_id: int,
        amount: float | None = None,
        unit: str | None = None,
        preparation: str | None = None,
    ) -> RecipeIngredient | None:

        item = await self.get_recipe_ingredient(
            db,
            recipe_ingredient_id
        )

        if item is None:
            return None

        if amount is not None:
            item.amount = amount

        if unit is not None:
            item.unit = unit

        if preparation is not None:
            item.preparation = preparation

        await db.commit()
        await db.refresh(item)

        return item

    async def delete_recipe_ingredient(
        self,
        db: AsyncSession,
        recipe_ingredient_id: int,
    ) -> bool:

        item = await self.get_recipe_ingredient(
            db,
            recipe_ingredient_id
        )

        if item is None:
            return False

        await db.delete(item)
        await db.commit()

        return True
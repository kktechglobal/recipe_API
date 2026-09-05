from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.ingredient.models import Ingredient


class IngredientService:

    async def create_ingredient(
        self,
        db: AsyncSession,
        name: str,
        retrieve: str | None = None,
    ) -> Ingredient:

        ingredient = Ingredient(
            name=name,
            retrieve=retrieve,
        )

        db.add(ingredient)
        await db.commit()
        await db.refresh(ingredient)

        return ingredient

    async def get_ingredients(
        self,
        db: AsyncSession,
    ) -> list[Ingredient]:

        result = await db.execute(
            select(Ingredient).order_by(Ingredient.name)
        )

        return list(result.scalars().all())

    async def get_ingredient(
        self,
        db: AsyncSession,
        ingredient_id: int,
    ) -> Ingredient | None:

        result = await db.execute(
            select(Ingredient)
            .where(Ingredient.id == ingredient_id)
        )

        return result.scalar_one_or_none()

    async def update_ingredient(
        self,
        db: AsyncSession,
        ingredient_id: int,
        name: str | None = None,
        retrieve: str | None = None,
    ) -> Ingredient | None:

        ingredient = await self.get_ingredient(
            db,
            ingredient_id
        )

        if ingredient is None:
            return None

        if name is not None:
            ingredient.name = name

        if retrieve is not None:
            ingredient.retrieve = retrieve

        await db.commit()
        await db.refresh(ingredient)

        return ingredient

    async def delete_ingredient(
        self,
        db: AsyncSession,
        ingredient_id: int,
    ) -> bool:

        ingredient = await self.get_ingredient(
            db,
            ingredient_id
        )

        if ingredient is None:
            return False

        await db.delete(ingredient)
        await db.commit()

        return True
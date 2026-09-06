from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.Recipe.models import Recipe
from app.RecipeStep.models import RecipeStep


class RecipeStepService:

    async def create_step(
        self,
        db: AsyncSession,
        recipe_id: int,
        step_number: int,
        instruction: str,
        user_id: int,
    ) -> RecipeStep | None:

        # Check that the recipe belongs to the current user
        result = await db.execute(
            select(Recipe).where(
                Recipe.id == recipe_id,
                Recipe.user_id == user_id,
            )
        )

        recipe = result.scalar_one_or_none()

        if recipe is None:
            return None

        step = RecipeStep(
            recipe_id=recipe_id,
            step_number=step_number,
            instruction=instruction,
        )

        db.add(step)

        await db.commit()
        await db.refresh(step)

        return step


    async def get_steps(
        self,
        db: AsyncSession,
        recipe_id: int,
    ) -> list[RecipeStep]:

        result = await db.execute(
            select(RecipeStep)
            .where(
                RecipeStep.recipe_id == recipe_id
            )
            .order_by(RecipeStep.step_number)
        )

        return list(result.scalars().all())


    async def get_step(
        self,
        db: AsyncSession,
        step_id: int,
    ) -> RecipeStep | None:

        result = await db.execute(
            select(RecipeStep)
            .where(
                RecipeStep.id == step_id
            )
        )

        return result.scalar_one_or_none()


    async def update_step(
        self,
        db: AsyncSession,
        step_id: int,
        step_number: int | None = None,
        instruction: str | None = None,
        user_id: int | None = None,
    ) -> RecipeStep | None:

        result = await db.execute(
            select(RecipeStep)
            .join(Recipe)
            .where(
                RecipeStep.id == step_id,
                Recipe.user_id == user_id,
            )
        )

        step = result.scalar_one_or_none()

        if step is None:
            return None

        if step_number is not None:
            step.step_number = step_number

        if instruction is not None:
            step.instruction = instruction

        await db.commit()
        await db.refresh(step)

        return step


    async def delete_step(
        self,
        db: AsyncSession,
        step_id: int,
        user_id: int | None = None,
    ) -> bool:

        result = await db.execute(
            select(RecipeStep)
            .join(Recipe)
            .where(
                RecipeStep.id == step_id,
                Recipe.user_id == user_id,
            )
        )

        step = result.scalar_one_or_none()

        if step is None:
            return False

        await db.delete(step)
        await db.commit()

        return True








# from sqlalchemy import select

# from sqlalchemy.ext.asyncio import AsyncSession

# from app.RecipeStep.models import RecipeStep


# class RecipeStepService:

#     async def create_step(
#         self,
#         db: AsyncSession,
#         recipe_id: int,
#         step_number: int,
#         instruction: str,
#     ) -> RecipeStep:

#         step = RecipeStep(
#             recipe_id=recipe_id,
#             step_number=step_number,
#             instruction=instruction,
#         )

#         db.add(step)
#         await db.commit()
#         await db.refresh(step)

#         return step

#     async def get_steps(
#         self,
#         db: AsyncSession,
#         recipe_id: int,
#     ) -> list[RecipeStep]:

#         result = await db.execute(
#             select(RecipeStep)
#             .where(RecipeStep.recipe_id == recipe_id)
#             .order_by(RecipeStep.step_number)


#         )

#         return list(result.scalars().all())

#     async def get_step(
#         self,
#         db: AsyncSession,
#         step_id: int,
#     ) -> RecipeStep | None:

#         result = await db.execute(
#             select(RecipeStep)
#             .where(RecipeStep.id == step_id)
#         )

#         return result.scalar_one_or_none()

#     async def update_step(
#         self,
#         db: AsyncSession,
#         step_id: int,
#         step_number: int | None = None,
#         instruction: str | None = None,
#     ) -> RecipeStep | None:

#         step = await self.get_step(db, step_id)

#         if step is None:
#             return None

#         if step_number is not None:
#             step.step_number = step_number

#         if instruction is not None:
#             step.instruction = instruction

#         await db.commit()
#         await db.refresh(step)

#         return step

#     async def delete_step(
#         self,
#         db: AsyncSession,
#         step_id: int,
#     ) -> bool:

#         step = await self.get_step(db, step_id)

#         if step is None:
#             return False

#         await db.delete(step)
#         await db.commit()

#         return True
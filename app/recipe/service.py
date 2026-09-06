from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.Recipe.models import Recipe
from app.Recipe.schema import RecipeCreate, RecipeUpdate


class RecipeService:












    async def create_recipe(
        self,
        db: AsyncSession,
        recipe_in: RecipeCreate,
        user_id: int,
    ) -> Recipe:

        recipe = Recipe(
            name=recipe_in.name,
            description=recipe_in.description,
            instructions=recipe_in.instructions,
            category_id=recipe_in.category_id,
            preparation=recipe_in.preparation,
            search=recipe_in.search,
            cooking_time=recipe_in.cooking_time,
            user_id=user_id,
        )

        db.add(recipe)

        await db.commit()
        await db.refresh(recipe)

        return recipe


    async def get_recipes(
        self,
        db: AsyncSession,
    ) -> list[Recipe]:

        result = await db.execute(
            select(Recipe)
        )

        return list(result.scalars().all())


    async def get_recipe(
        self,
        db: AsyncSession,
        recipe_id: int,
    ) -> Recipe | None:

        result = await db.execute(
            select(Recipe).where(
                Recipe.id == recipe_id
            )
        )

        return result.scalar_one_or_none()


    async def update_recipe(
        self,
        db: AsyncSession,
        recipe_id: int,
        recipe_in: RecipeUpdate,
        user_id: int,
    ) -> Recipe | None:

        result = await db.execute(
            select(Recipe).where(
                Recipe.id == recipe_id,
                Recipe.user_id == user_id,
            )
        )

        recipe = result.scalar_one_or_none()

        if recipe is None:
            return None

        update_data = recipe_in.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(recipe, field, value)

        await db.commit()
        await db.refresh(recipe)

        return recipe




#================
#search
#==================
async def search_recipes(
    self,
    db: AsyncSession,
    name: str,
) -> list[Recipe]:

    result = await db.execute(
        select(Recipe).where(
            Recipe.name.ilike(f"%{name}%")
        )
    )

    return list(result.scalars().all())

#=================================================

    async def delete_recipe(
        self,
        db: AsyncSession,
        recipe_id: int,
        user_id: int,
    ) -> bool:

        result = await db.execute(
            select(Recipe).where(
                Recipe.id == recipe_id,
                Recipe.user_id == user_id,
            )
        )

        recipe = result.scalar_one_or_none()

        if recipe is None:
            return False

        await db.delete(recipe)
        await db.commit()

        return True


    


# from sqlalchemy import select
# from sqlalchemy.ext.asyncio import AsyncSession

# from app.Recipe.models import Recipe
# from app.Recipe.schema import RecipeCreate, RecipeUpdate


# class RecipeService:

#     async def create_recipe(
#         self,
#         db: AsyncSession,
#         recipe_in: RecipeCreate
#     ) -> Recipe:

#         recipe = Recipe(
#             name=recipe_in.name,
#             description=recipe_in.description,
#             instructions=recipe_in.instructions,
#             category_id=recipe_in.category_id,
#             preparation=recipe_in.preparation,
#             search=recipe_in.search,
#             cooking_time=recipe_in.cooking_time
#         )

#         db.add(recipe)

#         await db.commit()
#         await db.refresh(recipe)

#         return recipe

#     async def get_recipes(
#         self,
#         db: AsyncSession
#     ) -> list[Recipe]:

#         result = await db.execute(
#             select(Recipe)
#         )

#         return list(result.scalars().all())

#     async def get_recipe(
#         self,
#         db: AsyncSession,
#         recipe_id: int
#     ) -> Recipe | None:

#         result = await db.execute(
#             select(Recipe).where(
#                 Recipe.id == recipe_id
#             )
#         )

#         return result.scalar_one_or_none()

#     async def update_recipe(
#         self,
#         db: AsyncSession,
#         recipe_id: int,
#         recipe_in: RecipeUpdate
#     ) -> Recipe | None:

#         recipe = await self.get_recipe(
#             db,
#             recipe_id
#         )

#         if recipe is None:
#             return None

#         update_data = recipe_in.model_dump(
#             exclude_unset=True
#         )

#         for field, value in update_data.items():
#             setattr(recipe, field, value)

#         await db.commit()
#         await db.refresh(recipe)

#         return recipe

#     async def delete_recipe(
#         self,
#         db: AsyncSession,
#         recipe_id: int
#     ) -> bool:

#         recipe = await self.get_recipe(
#             db,
#             recipe_id
#         )

#         if recipe is None:
#             return False

#         await db.delete(recipe)
#         await db.commit()

#         return True

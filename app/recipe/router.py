from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import get_current_user
from app.database.db import get_session

from app.Recipe.schema import (
    RecipeCreate,
    RecipeUpdate,
    RecipeResponse,
)

from app.Recipe.service import RecipeService
from app.user.models import User


router = APIRouter(
    prefix="/recipes",
    tags=["Recipes"],
)

service = RecipeService()


# =========================
# CREATE
# =========================

@router.post(
    "/",
    response_model=RecipeResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_recipe(
    recipe_in: RecipeCreate,
    db: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    return await service.create_recipe(
        db,
        recipe_in,
        current_user.id,
    )


# =========================
# GET ALL
# =========================

@router.get(
    "/",
    response_model=list[RecipeResponse],
)
async def get_recipes(
    db: AsyncSession = Depends(get_session),
):
    return await service.get_recipes(db)


#================== 
#saerch
#=================
@router.get(
    "/search",
    response_model=list[RecipeResponse],
)
async def search_recipes(
    name: str,
    db: AsyncSession = Depends(get_session),
):
    return await service.search_recipes(
        db,
        name,
    )


# =========================
# GET ONE
# =========================

@router.get(
    "/{recipe_id}",
    response_model=RecipeResponse,
)
async def get_recipe(
    recipe_id: int,
    db: AsyncSession = Depends(get_session),
):
    recipe = await service.get_recipe(
        db,
        recipe_id,
    )

    if recipe is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe not found",
        )

    return recipe


# =========================
# UPDATE
# =========================

@router.put(
    "/{recipe_id}",
    response_model=RecipeResponse,
)
async def update_recipe(
    recipe_id: int,
    recipe_in: RecipeUpdate,
    db: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    recipe = await service.update_recipe(
        db,
        recipe_id,
        recipe_in,
        current_user.id,
    )

    if recipe is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe not found",
        )

    return recipe


# =========================
# DELETE
# =========================

@router.delete(
    "/{recipe_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_recipe(
    recipe_id: int,
    db: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    deleted = await service.delete_recipe(
        db,
        recipe_id,
        current_user.id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe not found",
        )

    return None






# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.ext.asyncio import AsyncSession

# from app.database.db import get_session

# from app.Recipe.schema import (
#     RecipeCreate,
#     RecipeUpdate,
#     RecipeResponse
# )

# from app.Recipe.service import RecipeService


# router = APIRouter(
#     prefix="/recipes",
#     tags=["Recipes"]
# )

# service = RecipeService()


# # =========================
# # CREATE
# # =========================

# @router.post(
#     "/",
#     response_model=RecipeResponse,
#     status_code=status.HTTP_201_CREATED
# )
# async def create_recipe(
#     recipe_in: RecipeCreate,
#     db: AsyncSession = Depends(get_session)
# ):
#     return await service.create_recipe(
#         db,
#         recipe_in
#     )


# # =========================
# # GET ALL
# # =========================

# @router.get(
#     "/",
#     response_model=list[RecipeResponse]
# )
# async def get_recipes(
#     db: AsyncSession = Depends(get_session)
# ):
#     return await service.get_recipes(db)


# # =========================
# # GET ONE
# # =========================

# @router.get(
#     "/{recipe_id}",
#     response_model=RecipeResponse
# )
# async def get_recipe(
#     recipe_id: int,
#     db: AsyncSession = Depends(get_session)
# ):

#     recipe = await service.get_recipe(
#         db,
#         recipe_id
#     )

#     if recipe is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Recipe not found"
#         )

#     return recipe


# # =========================
# # UPDATE
# # =========================

# @router.put(
#     "/{recipe_id}",
#     response_model=RecipeResponse
# )
# async def update_recipe(
#     recipe_id: int,
#     recipe_in: RecipeUpdate,
#     db: AsyncSession = Depends(get_session)
# ):

#     recipe = await service.update_recipe(
#         db,
#         recipe_id,
#         recipe_in
#     )

#     if recipe is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Recipe not found"
#         )

#     return recipe


# # =========================
# # DELETE
# # =========================

# @router.delete(
#     "/{recipe_id}",
#     status_code=status.HTTP_204_NO_CONTENT
# )
# async def delete_recipe(
#     recipe_id: int,
#     db: AsyncSession = Depends(get_session)
# ):

#     deleted = await service.delete_recipe(
#         db,
#         recipe_id
#     )

#     if not deleted:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Recipe not found"
#         )

#     return None
























# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.ext.asyncio import AsyncSession

# from app.database.db import get_db

# from app.Recipe.schema import (
#     RecipeCreate,
#     RecipeUpdate,
#     RecipeResponse
# )

# from app.Recipe.service import RecipeService


# router = APIRouter(
#     prefix="/recipes",
#     tags=["Recipes"]
# )

# service = RecipeService()


# # =========================
# # CREATE RECIPE
# # =========================

# @router.post(
#     "/",
#     response_model=RecipeResponse,
#     status_code=status.HTTP_201_CREATED
# )
# async def create_recipe(
#     recipe_in: RecipeCreate,
#     db: AsyncSession = Depends(get_db)
# ):
#     return await service.create_recipe(
#         db,
#         recipe_in
#     )


# # =========================
# # GET ALL RECIPES
# # =========================

# @router.get(
#     "/",
#     response_model=list[RecipeResponse]
# )
# async def get_recipes(
#     db: AsyncSession = Depends(get_db)
# ):
#     return await service.get_recipes(db)


# # =========================
# # GET ONE RECIPE
# # =========================

# @router.get(
#     "/{recipe_id}",
#     response_model=RecipeResponse
# )
# async def get_recipe(
#     recipe_id: int,
#     db: AsyncSession = Depends(get_db)
# ):

#     recipe = await service.get_recipe(
#         db,
#         recipe_id
#     )

#     if recipe is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Recipe not found"
#         )

#     return recipe


# # =========================
# # UPDATE RECIPE
# # =========================

# @router.put(
#     "/{recipe_id}",
#     response_model=RecipeResponse
# )
# async def update_recipe(
#     recipe_id: int,
#     recipe_in: RecipeUpdate,
#     db: AsyncSession = Depends(get_db)
# ):

#     recipe = await service.update_recipe(
#         db,
#         recipe_id,
#         recipe_in
#     )

#     if recipe is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Recipe not found"
#         )

#     return recipe


# # =========================
# # DELETE RECIPE
# # =========================

# @router.delete(
#     "/{recipe_id}",
#     status_code=status.HTTP_204_NO_CONTENT
# )
# async def delete_recipe(
#     recipe_id: int,
#     db: AsyncSession = Depends(get_db)
# ):

#     deleted = await service.delete_recipe(
#         db,
#         recipe_id
#     )

#     if not deleted:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Recipe not found"
#         )

#     return None

















# from fastapi import APIRouter, Depends, Query, status
# from sqlalchemy.ext.asyncio import AsyncSession


# #from app.database.db import get_db
# from app.Recipe.schema import RecipeCreate, RecipeUpdate, RecipeResponse, RecipeIngredientResponse
# from app.Recipe.service import RecipeService

# router = APIRouter(prefix="/Recipes", tags=["Recipes"])


# # def format_recipe_response(recipe) -> dict:
# #     ingredients_list = [
# #         RecipeIngredientResponse(
# #             id=ri.id,
# #             name=ri.ingredient.name,
# #             amount=ri.amount,
# #             unit=ri.unit,
# #             preparation=ri.preparation,
# #         )
# #         for ri in recipe.recipe_ingredients
# #     ]
# #     return {
# #         "id": recipe.id,
# #         "name": recipe.name,
# #         "description": recipe.description,
# #         "category": recipe.category.name if recipe.category else None,
# #         "prep_minutes": recipe.prep_minutes,
# #         "cook_minutes": recipe.cook_minutes,
# #         "ingredients": ingredients_list,
# #         "instructions": recipe.instructions,
# #     }


# @router.post("", response_model=RecipeResponse, status_code=status.HTTP_201_CREATED)
# async def create_recipe(
#     recipe_in: RecipeCreate,
#     db: AsyncSession = Depends#(get_db),
# ):
#     recipe = await RecipeService.create_recipe(db, recipe_in)
#     return format_recipe_response(recipe)


# @router.get("", response_model=list[RecipeResponse])
# async def search_recipes(
#     search: str | None = None,
#     category: str | None = None,
#     ingredient: list[str] = Query(default=[]),
#     max_time: int | None = Query(default=None, description="Max total cook + prep time in minutes"),
#     skip: int = 0,
#     limit: int = 10,
#     db: AsyncSession = Depends#(get_db),
# ):
#     recipes = await RecipeService.search_recipes(
#         db, search, category, ingredient, max_time, skip, limit
#     )
#     return [format_recipe_response(r) for r in recipes]


# @router.get("/{recipe_id}", response_model=RecipeResponse)
# async def get_recipe(
#     recipe_id: int,
#     db: AsyncSession = Depends#(get_db),
# ):
#     recipe = await RecipeService.get_recipe_by_id(db, recipe_id)
#     return format_recipe_response(recipe)


# @router.put("/{recipe_id}", response_model=RecipeResponse)
# async def update_recipe(
#     recipe_id: int,
#     recipe_in: RecipeUpdate,
#     db: AsyncSession = Depends#(get_db),
# ):
#     updated = await RecipeService.update_recipe(db, recipe_id, recipe_in)
#     return format_recipe_response(updated)


# @router.delete("/{recipe_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_recipe(
#     recipe_id: int,
#     db: AsyncSession = Depends#(get_db),
# ):
#     await RecipeService.delete_recipe(db, recipe_id)
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import get_current_user
from app.database.db import get_session
from app.RecipeStep.service import RecipeStepService
from app.user.models import User


router = APIRouter(
    prefix="/recipes",
    tags=["Recipe Steps"],
)

service = RecipeStepService()


class RecipeStepCreate(BaseModel):
    step_number: int
    instruction: str


class RecipeStepUpdate(BaseModel):
    step_number: int | None = None
    instruction: str | None = None


# =========================
# CREATE STEP
# =========================

@router.post(
    "/{recipe_id}/steps",
    status_code=status.HTTP_201_CREATED,
)
async def create_step(
    recipe_id: int,
    step_data: RecipeStepCreate,
    db: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    step = await service.create_step(
        db,
        recipe_id,
        step_data.step_number,
        step_data.instruction,
        current_user.id,
    )

    if step is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe not found",
        )

    return step


# =========================
# GET STEPS
# =========================

@router.get("/{recipe_id}/steps")
async def get_steps(
    recipe_id: int,
    db: AsyncSession = Depends(get_session),
):
    return await service.get_steps(db, recipe_id)


# =========================
# GET ONE STEP
# =========================

@router.get("/steps/{step_id}")
async def get_step(
    step_id: int,
    db: AsyncSession = Depends(get_session),
):
    step = await service.get_step(db, step_id)

    if step is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe step not found",
        )

    return step


# =========================
# UPDATE STEP
# =========================

@router.put("/steps/{step_id}")
async def update_step(
    step_id: int,
    step_data: RecipeStepUpdate,
    db: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    step = await service.update_step(
        db,
        step_id,
        step_data.step_number,
        step_data.instruction,
        current_user.id,
    )

    if step is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe step not found",
        )

    return step


# =========================
# DELETE STEP
# =========================

@router.delete(
    "/steps/{step_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_step(
    step_id: int,
    db: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    deleted = await service.delete_step(
        db,
        step_id,
        current_user.id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe step not found",
        )

    return None








# from fastapi import APIRouter, Depends, HTTPException, status
# from pydantic import BaseModel
# from sqlalchemy.ext.asyncio import AsyncSession

# from app.database.db import get_session
# from app.RecipeStep.service import RecipeStepService


# router = APIRouter(
#     prefix="/recipes",
#     tags=["Recipe Steps"]
# )

# service = RecipeStepService()


# class RecipeStepCreate(BaseModel):
#     step_number: int
#     instruction: str


# class RecipeStepUpdate(BaseModel):
#     step_number: int | None = None
#     instruction: str | None = None


# @router.post(
#     "/{recipe_id}/steps",
#     status_code=status.HTTP_201_CREATED
# )
# async def create_step(
#     recipe_id: int,
#     step_data: RecipeStepCreate,
#     db: AsyncSession = Depends(get_session),
# ):
#     return await service.create_step(
#         db,
#         recipe_id,
#         step_data.step_number,
#         step_data.instruction,
#     )


# @router.get("/{recipe_id}/steps")
# async def get_steps(
#     recipe_id: int,
#     db: AsyncSession = Depends(get_session),
# ):
#     return await service.get_steps(db, recipe_id)


# @router.get("/steps/{step_id}")
# async def get_step(
#     step_id: int,
#     db: AsyncSession = Depends(get_session),
# ):
#     step = await service.get_step(db, step_id)

#     if step is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Recipe step not found",
#         )

#     return step


# @router.put("/steps/{step_id}")
# async def update_step(
#     step_id: int,
#     step_data: RecipeStepUpdate,
#     db: AsyncSession = Depends(get_session),
# ):
#     step = await service.update_step(
#         db,
#         step_id,
#         step_data.step_number,
#         step_data.instruction,
#     )

#     if step is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Recipe step not found",
#         )

#     return step


# @router.delete(
#     "/steps/{step_id}",
#     status_code=status.HTTP_204_NO_CONTENT
# )
# async def delete_step(
#     step_id: int,
#     db: AsyncSession = Depends(get_session),
# ):
#     deleted = await service.delete_step(db, step_id)

#     if not deleted:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Recipe step not found",
#         )

#     return None
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.db import get_session
from app.category.service import CategoryService


router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

service = CategoryService()


class CategoryCreate(BaseModel):
    name: str


class CategoryUpdate(BaseModel):
    name: str


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED
)
async def create_category(
    category_data: CategoryCreate,
    db: AsyncSession = Depends(get_session),
):
    return await service.create_category(
        db,
        category_data.name
    )


@router.get("/")
async def get_categories(
    db: AsyncSession = Depends(get_session),
):
    return await service.get_categories(db)


@router.get("/{category_id}")
async def get_category(
    category_id: int,
    db: AsyncSession = Depends(get_session),
):
    category = await service.get_category(
        db,
        category_id
    )

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )

    return category


@router.put("/{category_id}")
async def update_category(
    category_id: int,
    category_data: CategoryUpdate,
    db: AsyncSession = Depends(get_session),
):
    category = await service.update_category(
        db,
        category_id,
        category_data.name
    )

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )

    return category


@router.delete(
    "/{category_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_category(
    category_id: int,
    db: AsyncSession = Depends(get_session),
):
    deleted = await service.delete_category(
        db,
        category_id
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )

    return None
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.category.models import Category


class CategoryService:

    async def create_category(
        self,
        db: AsyncSession,
        name: str,
    ) -> Category:

        category = Category(name=name)

        db.add(category)
        await db.commit()
        await db.refresh(category)

        return category

    async def get_categories(
        self,
        db: AsyncSession,
    ) -> list[Category]:

        result = await db.execute(
            select(Category).order_by(Category.name)
        )

        return list(result.scalars().all())

    async def get_category(
        self,
        db: AsyncSession,
        category_id: int,
    ) -> Category | None:

        result = await db.execute(
            select(Category)
            .where(Category.id == category_id)
        )

        return result.scalar_one_or_none()

    async def update_category(
        self,
        db: AsyncSession,
        category_id: int,
        name: str,
    ) -> Category | None:

        category = await self.get_category(
            db,
            category_id
        )

        if category is None:
            return None

        category.name = name

        await db.commit()
        await db.refresh(category)

        return category

    async def delete_category(
        self,
        db: AsyncSession,
        category_id: int,
    ) -> bool:

        category = await self.get_category(
            db,
            category_id
        )

        if category is None:
            return False

        await db.delete(category)
        await db.commit()

        return True
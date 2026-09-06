from datetime import datetime
from typing import Optional, TYPE_CHECKING

from sqlalchemy import String, Float, DateTime, Integer, JSON, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


if TYPE_CHECKING:
    from app.user.models import User
    from app.category.models import Category
    from app.RecipeStep.models import RecipeStep
    from app.RecipeIngredient.models import RecipeIngredient


class Recipe(Base):
    __tablename__ = "Recipe"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(50),nullable=False )

    description: Mapped[str] = mapped_column(String(500),nullable=False)

    instructions: Mapped[list[str]] = mapped_column(JSON,nullable=False)

    preparation: Mapped[Optional[str]] = mapped_column(String(1000),nullable=True)

    search: Mapped[Optional[str]] = mapped_column(String(1000),nullable=True)

    cooking_time: Mapped[float] = mapped_column(Float,nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now())
    

    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"),nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"),nullable=False)
# ======================================
# relationships
# ====================================
    user: Mapped["User"] = relationship(back_populates="recipes")

    category: Mapped["Category"] = relationship(back_populates="recipes")

    recipe_steps: Mapped[list["RecipeStep"]] = relationship(back_populates="recipe",cascade="all, delete-orphan")

    recipe_ingredients: Mapped[list["RecipeIngredient"]] = relationship(back_populates="recipe",cascade="all, delete-orphan")



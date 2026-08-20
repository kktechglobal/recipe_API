from datetime import datetime, DateTime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, func, primary_key,string
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.recipes import recipe
    from app.models.category import Category
    from app.models.recipe_step import recipe_step
    

class Recipe(Base):
    __tablename__ = "recipe"
    id: Mapped[int] = mapped_column(primary_key=True, )
    name: Mapped[str] = mapped_column(string(50),nullable=False)
    description: Mapped[str] = mapped_column(string(500),nullable=False)
    instructions: Mapped[str] = mapped_column(string(1000),nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())



    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)

    category: Mapped["Category"] = relationship(back_populates="recipe")
    step: Mapped[list["recipe_step"]] = relationship("RecipeStep", back_populates="recipe", cascade="all, delete-orphan")

    #user
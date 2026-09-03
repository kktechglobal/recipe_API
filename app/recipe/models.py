from datetime import datetime
from typing import TYPE_CHECKING, Optional




from sqlalchemy import ForeignKey, func,String, Float,DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.recipe import category
    from app.recipe import recipe_step
        
    from app.recipe.models import recipe
    from app.recipe.models import category
    from app.recipe.models import recipe_step
    

class Recipe(Base):
    __tablename__ = "recipe"
    id: Mapped[int] = mapped_column(primary_key=True, )
    name: Mapped[str] = mapped_column(String(50),nullable=False)
    description: Mapped[str] = mapped_column(String(500),nullable=False)
    instructions: Mapped[str] = mapped_column(String(1000),nullable=False)
    preparation : Mapped[Optional[str]] = mapped_column(String(1000),nullable=True)
    cooking_time: Mapped[float] = mapped_column(Float,nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())



    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)

    category: Mapped["category"] = relationship(back_populates="recipe")
    step: Mapped[list["recipe_step"]] = relationship("RecipeStep", back_populates="recipe", cascade="all, delete-orphan")

    #user
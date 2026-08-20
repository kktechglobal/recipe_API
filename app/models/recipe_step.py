from datetime import datetime, DateTime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, func, primary_key,string,integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.recipes import recipes
    from app.models.category import Category





class RecipeStep(Base):
    __tablename__ = "recipe_steps"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.id", ondelete="CASCADE"), nullable=False)
    step_number: Mapped[int] = mapped_column(integer, nullable=False)
    instruction: Mapped[str] = mapped_column(string, nullable=False)

    recipe: Mapped["recipes"] = relationship(back_populates="steps")
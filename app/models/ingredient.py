from datetime import datetime
from typing import TYPE_CHECKING


from sqlalchemy import ForeignKey,String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship, string

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.category import Category
    from app.models.recipe_ingredient import recipe_ingredient

class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100),index=True)



    

    ingredient: Mapped["Ingredient"] = relationship(back_populates="recipe_ingredients")

    recipe_ingredients: Mapped[list["recipe_ingredient"]] = relationship("recipe_ingredient", back_populates="ingredient")
from datetime import datetime
from typing import TYPE_CHECKING




from sqlalchemy import ForeignKey,String
from sqlalchemy import String, Float, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base

if TYPE_CHECKING:
    from app.recipe.models import Recipe
    from app.ingredient.models import Ingredient

class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100),index=True)
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipe.id", ), index=True)
    ingredient_id: Mapped[int] = mapped_column(ForeignKey("ingredients.id", index=True))
    amount: Mapped[float | None] = mapped_column(float, nullable=True)
    unit: Mapped[str] = mapped_column(String(20))
    preparation: Mapped[str | None] = mapped_column(String(100), nullable=True)



    recipes: Mapped["Recipe"] = relationship(back_populates="ingredients")
    
    ingredient: Mapped["Ingredient"] = relationship(back_populates="recipe")


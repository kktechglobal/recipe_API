from typing import TYPE_CHECKING



from sqlalchemy import String, Float, ForeignKey, Integer, primary_key
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base




if TYPE_CHECKING:
    from app.models.recipes import recipes
    from app.models.ingredient import ingredient

class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"

    id: Mapped[int] = mapped_column(primary_key=True)
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipe.id", ), index=True)
    ingredient_id: Mapped[int] = mapped_column(ForeignKey("ingredients.id", index=True))
    amount: Mapped[float | None] = mapped_column(Float, nullable=True)
    unit: Mapped[str] = mapped_column(String(20))
    preparation: Mapped[str | None] = mapped_column(String(100), nullable=True)



    ingredient: Mapped["ingredient"] = relationship(back_populates="recipe_ingredients")
    recipes: Mapped["recipes"] = relationship(back_populates="recipe_ingredients")
    #user:
    
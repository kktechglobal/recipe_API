from typing import TYPE_CHECKING

from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


if TYPE_CHECKING:
    from app.Recipe.models import Recipe
    from app.ingredient.models import Ingredient


class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    recipe_id: Mapped[int] = mapped_column(
        ForeignKey("Recipe.id", ondelete="CASCADE"),
        nullable=False
    )

    ingredient_id: Mapped[int] = mapped_column(
        ForeignKey("ingredients.id", ondelete="RESTRICT"),
        nullable=False
    )

    amount: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    unit: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    preparation: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    recipe: Mapped["Recipe"] = relationship(
        back_populates="recipe_ingredients"
    )

    ingredient: Mapped["Ingredient"] = relationship(
        back_populates="recipe_ingredients"
    )













# from datetime import datetime
# from typing import TYPE_CHECKING, Optional

# from sqlalchemy import Float
# from sqlalchemy import ForeignKey, func,String,DateTime
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
# from sqlalchemy.orm import relationship

# from app.database.base import Base
# from app.ingredient.models import Ingredient

# if TYPE_CHECKING:
        
#     from app.RecipeIngredient.models import RecipeIngredients

    


# class RecipeIngredient(Base):
#     __tablename__ = "recipe_ingredients"
#     id: Mapped[int] = mapped_column(primary_key=True)
    
#     recipe_id: Mapped[int] = mapped_column(ForeignKey("Recipe.id", ondelete="CASCADE"))
#     #ingredient_id: Mapped[int] = mapped_column(ForeignKey("Ingredient.id", ondelete="RESTRICT"), index=True)
#     amount: Mapped[float | None] = mapped_column(Float, nullable=True)
#     unit: Mapped[str] = mapped_column(String(50))
#     preparation: Mapped[str | None] = mapped_column(String(100), nullable=True)
    
    
#     ingredient: Mapped["RecipeIngredient"] = relationship( back_populates="Recipe")
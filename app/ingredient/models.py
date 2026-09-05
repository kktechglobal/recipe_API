from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


if TYPE_CHECKING:
    from app.RecipeIngredient.models import RecipeIngredient


class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
        index=True
    )

    retrieve: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    recipe_ingredients: Mapped[list["RecipeIngredient"]] = relationship(
        back_populates="ingredient"
    )



# from datetime import datetime
# from typing import TYPE_CHECKING




# from sqlalchemy import ForeignKey,String
# from sqlalchemy import String, Float, ForeignKey, Integer
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from app.database.base import Base

# if TYPE_CHECKING:
#     from app.recipe.models import Recipe
#     from app.ingredient.models import Ingredient

# class Ingredient(Base):
#     __tablename__ = "ingredients"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(100),index=True)
#     retrieve: Mapped[str] = mapped_column(String(500),nullable=True)
    



#     recipes: Mapped["Recipe"] = relationship(back_populates="ingredients")
#     ingredient: Mapped[list["Ingredient"]] = relationship(back_populates="recipe")


from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


if TYPE_CHECKING:
    from app.RecipeIngredient.models import RecipeIngredient


class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(100),nullable=False,unique=True,index=True)

    retrieve: Mapped[str | None] = mapped_column(String(500),nullable=True)


    #========================
    #relationships
    #========================= 
    recipe_ingredients: Mapped[list["RecipeIngredient"]] = relationship(back_populates="ingredient")
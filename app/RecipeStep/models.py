from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


if TYPE_CHECKING:
    from app.Recipe.models import Recipe


class RecipeStep(Base):
    __tablename__ = "recipe_step"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    recipe_id: Mapped[int] = mapped_column(
        ForeignKey("Recipe.id", ondelete="CASCADE"),
        nullable=False
    )

    step_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    instruction: Mapped[str] = mapped_column(
        String(1000),
        nullable=False
    )

    #========================
    # relationship  
    # =========================

    recipe: Mapped["Recipe"] = relationship(
        back_populates="recipe_steps"
    )







# from typing import TYPE_CHECKING

# from sqlalchemy import ForeignKey, func,String,Integer
# from sqlalchemy.orm import DeclarativeBase, Mapped
# from sqlalchemy.orm import mapped_column
# from sqlalchemy.orm import relationship

# from app.database.base import Base

# if TYPE_CHECKING:
#     from app.Recipe.models import Recipe

#     class base (DeclarativeBase):
#         pass
    

# class RecipeStep(Base):
#     __tablename__ = "recipe_step"

#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     recipe_id: Mapped[int] = mapped_column(ForeignKey("Recipe.id"), nullable=False)
#     step_number: Mapped[int] = mapped_column(Integer, nullable=False)
#     instruction: Mapped[str] = mapped_column(String(1000), nullable=False)

#     recipe: Mapped["Recipe"] = relationship(back_populates="recipe_step")
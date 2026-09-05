from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


if TYPE_CHECKING:
    from app.Recipe.models import Recipe


class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(Integer,primary_key=True)

    name: Mapped[str] = mapped_column(String(100),nullable=False,unique=True)

    #========================
    # relationtionship
    # =========================
    recipes: Mapped[list["Recipe"]] = relationship(back_populates="category")


# from datetime import datetime
# from typing import TYPE_CHECKING


# from sqlalchemy import ForeignKey, Integer
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
# from sqlalchemy.orm import relationship

# from app.database.base import Base

# if TYPE_CHECKING:

#     from app.category.models import Category 

# class Category(Base):
#     __tablename__ = "category"
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     category_id: Mapped[int] = mapped_column(ForeignKey("Recipe.id"))


#     category: Mapped[list["Category"]]= relationship(back_populates ="recipe")
    
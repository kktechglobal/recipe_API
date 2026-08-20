from datetime import datetime
from typing import TYPE_CHECKING

from app.models import recipes
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.recipes import recipes
    from app.models.category import Category

class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("primary_key.id"))


    recipe: Mapped[list["recipes"]]= relationship("recipe",back_populate ="category")
    
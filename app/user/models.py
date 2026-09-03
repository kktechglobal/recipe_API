from datetime import datetime
from typing import TYPE_CHECKING
from app.database.base import Base


from sqlalchemy import String, DateTime, func
from sqlalchemy import String, Float, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base

if TYPE_CHECKING:
    from app.recipe.models import Recipe
    
    

class users(Base):
    __tablename__ = "users"


    id: Mapped[int] = mapped_column (primary_key= True, index= True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    
    #relationships  
    recipes: Mapped[list["Recipe"]] = relationship("Recipe", back_populates="users")











#recipe:
#recipe_ingredient:

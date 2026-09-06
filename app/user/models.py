from datetime import datetime
from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.Recipe.models import Recipe

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(String(50),nullable=False,unique=True,index=True)

    email: Mapped[str] = mapped_column(String(255),nullable=False,unique=True,index=True)

    password: Mapped[str] = mapped_column(String(255),nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now() )

    #======================================
    # relationships
    #======================================
    recipes: Mapped[list["Recipe"]] = relationship(back_populates="user")
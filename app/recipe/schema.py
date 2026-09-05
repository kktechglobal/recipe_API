from datetime import datetime

from pydantic import BaseModel, ConfigDict


# =========================
# RECIPE SCHEMAS
# =========================

class RecipeCreate(BaseModel):
    name: str
    description: str
    instructions: list[str]
    preparation: str | None = None
    search: str | None = None
    cooking_time: float


class RecipeUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    instructions: list[str] | None = None
    preparation: str | None = None
    search: str | None = None
    cooking_time: float | None = None


class RecipeResponse(BaseModel):
    id: int
    name: str
    description: str
    instructions: list[str]
    preparation: str | None = None
    search: str | None = None
    cooking_time: float
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
from pydantic import BaseModel, ConfigDict


# =========================
# RECIPE INGREDIENT SCHEMAS
# =========================

class RecipeIngredientCreate(BaseModel):
    name: str
    amount: float | None = None
    unit: str
    preparation: str | None = None


class RecipeIngredientUpdate(BaseModel):
    amount: float | None = None
    unit: str | None = None
    preparation: str | None = None


class RecipeIngredientResponse(BaseModel):
    id: int
    name: str
    amount: float | None
    unit: str
    preparation: str | None = None




    model_config = ConfigDict(from_attributes=True)
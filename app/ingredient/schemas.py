from pydantic import BaseModel, ConfigDict

class RecipeIngredientCreate(BaseModel):
    name: str  # Global ingredient name (e.g., "Flour")
    amount: float | None = None
    unit: str
    preparation: str | None = None

class RecipeIngredientUpdate(BaseModel):
    amount: float | None = None
    unit: str | None = None
    preparation: str | None = None

class RecipeIngredientResponse(BaseModel):
    id: int  # Points directly to the RecipeIngredient relationship ID
    name: str
    amount: float | None
    unit: str
    preparation: str | None = None

    model_config = ConfigDict(from_attributes=True)
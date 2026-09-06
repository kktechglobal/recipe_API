"""Application entry point.

Notice what is NOT here: no business logic, no SQL, no route bodies. main.py
only creates the app, defines its startup/shutdown, and plugs in the routers.
When a file's whole job fits on one screen, you can see the shape of the
project without reading any of it.
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.db import init_models, dispose_engine

from app.Recipe.router import router as Recipe
from app.RecipeStep.router import router as RecipeStep
from app.ingredient.router import router as Ingredient
from app.RecipeIngredient.router import router as RecipeIngredient
from app.category.routers import router as Category
from app.user.router import router as user


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs once when the application starts
    await init_models()

    yield

    # Runs once when the application shuts down
    await dispose_engine()


app = FastAPI(
    title="Recipe API",
    lifespan=lifespan
)

app.include_router(user)
app.include_router(Recipe)
app.include_router(RecipeStep)
app.include_router(Ingredient)
app.include_router(RecipeIngredient)
app.include_router(Category)


@app.get("/", tags=["meta"])
async def root():
    return {
        "status": "ok",
        "docs": "/docs"
    }
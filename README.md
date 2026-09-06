# recipe_API

<!-- <!-- <!-- stage
1 t0 2
1 to 3
1 to 4




Recipe Search Endpoint

The Recipe API allows users to search for recipes by their name.

Endpoint

"GET /recipes/search"

How to Use

Start the FastAPI server:

uvicorn app.main:app --reload

Then open the Swagger documentation:

http://127.0.0.1:8000/docs

Find:

GET /recipes/search

Click Try it out, enter the recipe name you want to search for, and click Execute.

Example

Search for recipes containing "rice":

GET /recipes/search?name=rice

The search is case-insensitive and can return recipes such as:

- Fried Rice
- Jollof Rice
- Coconut Rice -->

Response Example

[
  {
    "id": 1,
    "name": "Fried Rice",
    "description": "A simple fried rice recipe",
    "instructions": [
      "Cook the rice",
      "Add vegetables",
      "Fry the ingredients together"
    ],
    "preparation": "10 minutes",
    "search": "rice",
    "cooking_time": 30,
    "created_at": "2026-09-06T18:00:00"
  }
]

Search Logic

The endpoint uses a case-insensitive partial search. For example:

rice

can match:

Fried Rice
Jollof Rice
Coconut Rice

The search is performed using SQLAlchemy's "ilike()" function.
 -->

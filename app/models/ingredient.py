"""
Ingredient SQL Model.

This is the defintiion of the following SQL Model classes:
- Ingredient
- IngredientAmount
"""
from typing import Optional
from sqlmodel import SQLModel, Field


class Ingredent(SQLModel, table=True):
    """The Ingredient model."""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

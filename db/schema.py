from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String, Text, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    ingredients = relationship('RecipeIngredient', back_populates='recipe')

    def __repr__(self):
        return f'<Recipe {self.name}>'


class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredients'

    id = Column(Integer, primary_key=True)
    ingredient_id = relationship('Ingredient') # Fix for Foreign key stuff one to one
    amount = Column(Integer)
    unit = Column(String(255))
    recipe = relationship('Recipe', back_populates='ingredients')

    def __repr__(self):
        return f'<Recipe {self.recipe.name} - Ingredient {self.ingredient_id.name}>'


class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __repr__(self):
        return f'<Ingredient {self.name}>'

    
Recipe.ingredients = relationship('RecipeIngredient', order_by=RecipeIngredient.id, back_populates='recipe')
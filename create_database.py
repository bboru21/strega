import os
from simple_settings import settings
from peewee import *

db = MySQLDatabase(
    'scripts',
    user=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
)

from models import (
    Feasts,
    Ingredients,
    Cocktails,
    CocktailsToFeasts,
    IngredientsToCocktails,
)

from data import (
    FEASTS,
)

CONTROLLED_BEVERAGE_TYPES = [
    "gin",
    "bourbon",
    "brandy",
    "liqueur",
    "absinthe",
    "bitters",
    "rum",
    "vodka",
    "aperitif",
    "whiskey",
    "chocolate cherry liqueur",
    "vanilla flavored vodka",
    "coffee liqueur",
    "cream liqueur",
    "caramel flavored vodka",
    "dry vermouth",
    "sweet vermouth",
    "orange flavored liqueur",
    "orange bitters",
    "tequila blanco",
    "elderflower liqueur",
    "orange liqueur",
    "bitter herbal liqueur",
    "light rum",
    "sweet liqueur",
    "151-proof rum",
    "dry sparkling wine",
]

PURCHASED_BEVERAGE_TYPES = [
    "gin",
    "liqueur",
    "bitters",
    "vodka",
    "whiskey",
    "dry vermouth",
    "sweet vermouth",
    "orange flavored liqueur",
    "tequila blanco",
    "orange liqueur",
]

# Connect to our database.
db.connect()

tables = [Feasts, Ingredients, Cocktails, CocktailsToFeasts, IngredientsToCocktails]

db.drop_tables(tables)

# Create the tables.
db.create_tables(tables)

for feast in FEASTS:
    feast_date = '{}-{}'.format(settings.PLACEHOLDER_YEAR, feast.get('date'))
    feast_name = feast.get('name')
    cocktails = feast.get('cocktails', [])

    new_feast_id = Feasts.create( date=feast_date, name=feast_name )

    for cocktail in cocktails:
        cocktail_name = cocktail.get('name')
        ingredients = cocktail.get('ingredients')

        (new_cocktail_id, _) = Cocktails.get_or_create(name=cocktail_name)

        CocktailsToFeasts.create(
            cocktail=new_cocktail_id,
            feast=new_feast_id,
        )

        for ingredient in ingredients:
            ingredient_amount = ingredient.get('amount')
            ingredient_name = ingredient.get('name')
            ingredient_type = ingredient.get('type')

            # probably want to move this out, but keeping here for now
            is_controlled = (ingredient_type in CONTROLLED_BEVERAGE_TYPES)
            is_purchased = (ingredient_type in PURCHASED_BEVERAGE_TYPES)

            (new_ingredient_id, _) = Ingredients.get_or_create(
                name=ingredient_name,
                type=ingredient_type,
                is_controlled=is_controlled,
                is_purchased=is_purchased,
            )

            IngredientsToCocktails.create(
                ingredient=new_ingredient_id,
                cocktail=new_cocktail_id,
                amount=ingredient_amount,
            )

print 'finis'
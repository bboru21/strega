import os
from simple_settings import settings

from models import (
    Feasts,
    Ingredients,
    IngredientsToCocktails as Amounts,
    Cocktails,
    CocktailsToFeasts,
)

date_range = (
    '{}-05-01'.format(settings.PLACEHOLDER_YEAR),
    '{}-05-31'.format(settings.PLACEHOLDER_YEAR),
)

cocktails = Cocktails.select(Feasts.name.alias('feast_name'), Cocktails.name.alias('name'), Cocktails.cocktail_id.alias('id') ) \
    .join(CocktailsToFeasts) \
    .join(Feasts) \
    .where( (Feasts.date >= date_range[0]) and (Feasts.date <= date_range[1]))

for cocktail in cocktails:

    print cocktail.name

    ingredients = (Ingredients
        .select(Ingredients.name, Ingredients.type, Amounts.amount)
        .join(Amounts)
        .where(Amounts.cocktail_id == cocktail.id)
    )

    for ingredient in ingredients.tuples().iterator():
        print '\t%s (%s) - %s' % ( ingredient[0], ingredient[1], ingredient[2] )


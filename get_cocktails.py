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


def get_cocktails(is_purchased=None):

    cocktails = Cocktails.select(Feasts.name.alias('feast_name'), Cocktails.name.alias('name'), Cocktails.cocktail_id.alias('id') ) \
        .join(CocktailsToFeasts) \
        .join(Feasts) \
        .where( (Feasts.date >= date_range[0]) and (Feasts.date <= date_range[1]))

    return cocktails

def get_ingredients(cocktails):

    ingredients = []

    for cocktail in cocktails:

        query = (Ingredients
            .select(Ingredients.name, Ingredients.type, Amounts.amount)
            .join(Amounts)
            .where(Amounts.cocktail_id == cocktail.id, Ingredients.is_purchased == False, Ingredients.is_controlled == True)
        )

        for ingredient in query.tuples().iterator():
            print '\t%s (%s) - %s' % ( ingredient[0], ingredient[1], ingredient[2] )
            ingredients.append({
                'name': ingredient[0],
                'type': ingredient[1],
                'amount': ingredient[2],
            })

    return ingredients

cocktails = get_cocktails()
ingredients = get_ingredients(cocktails)
for ingredient in ingredients:
    print ingredient.get("name")


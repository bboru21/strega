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

class Feasts(Model):
    feast_id = AutoField( primary_key=True )
    name = TextField()
    date = DateTimeField()
    class Meta:
        database = db
        table_name = 'STREGA_FEASTS'

class Cocktails(Model):
    cocktail_id = AutoField( primary_key=True )
    name = TextField()
    class Meta:
        database = db
        table_name = 'STREGA_COCKTAILS'

class Ingredients(Model):
    ingredient_id = AutoField( primary_key=True )
    name = TextField()
    type = TextField()
    class Meta:
        database = db
        table_name = 'STREGA_INGREDIENTS'

class CocktailsToFeasts(Model):
    cocktail = ForeignKeyField(Cocktails)
    feast = ForeignKeyField(Feasts)

    class Meta:
        database = db
        primary_key = CompositeKey('cocktail', 'feast')
        table_name = 'STREGA_COCKTAILS_FEASTS'

class IngredientsToCocktails(Model):
    ingredient = ForeignKeyField(Ingredients)
    cocktail = ForeignKeyField(Cocktails)
    amount = TextField()

    class Meta:
        database = db
        primary_key = CompositeKey('ingredient', 'cocktail')
        table_name = 'STREGA_INGREDIENTS_COCKTAILS'
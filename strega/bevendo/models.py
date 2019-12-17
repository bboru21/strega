from django.db import models

class Cocktails(models.Model):
    name = models.CharField(max_length=255)

class Feasts(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField('date of feast')

class Ingredients(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    is_controlled = models.BooleanField(null=True)
    is_purchased = models.BooleanField(default=False)



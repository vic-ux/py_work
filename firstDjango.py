from django.db import models

class Product(models.Model):
    title       = models.TextFields()
    description = models.TextFields()
    price       = models.TextFields()
    summary     = models.TextFields()
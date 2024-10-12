from django.db import models

from foodie_app.models import Category


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    directions = models.TextField(null=True, blank=True)
    posted_date = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

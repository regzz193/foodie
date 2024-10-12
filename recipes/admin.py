from django.contrib import admin

from recipes.models import Recipe


# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "ingredients", "directions", "posted_date")

admin.site.register(Recipe, RecipeAdmin)


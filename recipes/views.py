from django.http import HttpResponse
from django.shortcuts import render

from recipes.models import Recipe


# Create your views here.
def recipes(request):
    recipe = Recipe.objects.all()
    return render(request, "recipes/recipes.html", {"recipes": recipe})


def search(request, recipe_id):
    search_recipes = Recipe.objects.get(id=recipe_id)
    return render(request, "recipes/search_recipe.html", {"search_recipe": search_recipes})
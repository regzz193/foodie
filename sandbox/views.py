from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from recipes.models import Recipe


# Create your views here.
def index(request):
    data = ["Pizza", "Pasta", "Bread", "Salad", "Sushi", "Jam","Pie"]
    context = {"foods": data}
    return render(request, "sandbox/index.html", context=context)

class RecipeListView(ListView):
    model = Recipe
    template_name = "sandbox/index.html"
    context_object_name = "recipes"


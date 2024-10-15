from django.core.exceptions.ValidationError import messages
from django.shortcuts import render

from foodie_app.forms import CategoryForm
from foodie_app.models import Category
from recipes.models import Recipe


# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request, "foodie_app/index.html", context={"categories": categories})


def recipes(request, category_id):
    recipe = Recipe.objects.filter(category=category_id)
    categories = Category.objects.get(pk=category_id)
    context = {"recipes": recipe, "categories": categories}
    return render(request, "foodie_app/recipes.html", context=context)

def add_category(request):
    form = CategoryForm(request.POST or None)
    return render(request,"foodie_app/add_category.html", context={"form": form})

from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path("<int:recipe_id>", views.search, name='search_recipe'),
]

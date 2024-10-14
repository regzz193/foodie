from django.urls import path

from sandbox import views
from sandbox.views import RecipeListView

urlpatterns = [
    path("", views.index, name="index"),
    path("recipes/", RecipeListView.as_view(), name="foods"),
]
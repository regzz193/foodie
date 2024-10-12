from django.urls import path
from foodie_app import views

urlpatterns = [
    path("", views.index, name="index"),
]

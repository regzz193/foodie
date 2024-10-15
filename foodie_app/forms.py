from django import forms

from foodie_app.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["names"]
        labels = {"names": "Category Names"}

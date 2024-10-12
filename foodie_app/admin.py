from django.contrib import admin

from foodie_app.models import Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date_added")
    search_fields = ("name",)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "ingredients", "directions", "posted_date")


admin.site.register(Category, CategoryAdmin)

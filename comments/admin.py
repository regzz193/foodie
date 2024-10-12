from django.contrib import admin

from comments.models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'text', 'date')


admin.site.register(Comment, CommentAdmin)
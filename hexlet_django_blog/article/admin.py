from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import Article


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ['article', 'body']
    list_filter = (('created_at', DateFieldListFilter),)

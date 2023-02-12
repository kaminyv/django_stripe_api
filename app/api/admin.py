from django.contrib import admin
from .models import Item


@admin.register(Item)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    fields = ['name', 'price', 'description']

from django.contrib import admin
from .models import Category, Recipe

class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'update_at')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)

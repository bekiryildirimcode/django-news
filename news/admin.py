from django.contrib import admin
from news.models import Category
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from mptt.admin import TreeRelatedFieldListFilter

@admin.register(Category)
class GenreAdmin(admin.ModelAdmin):
    model = Category
    list_filter =(('children', TreeRelatedFieldListFilter),)
    mptt_level_indent = 20
    list_display=(
        'name',
        'parent',
        'slug'
        
        # ...more fields if you feel like it...
    )

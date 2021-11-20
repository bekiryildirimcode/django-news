from django.contrib import admin
from news.models import Category,NewsModel
from django.utils.html import format_html
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from mptt.admin import TreeRelatedFieldListFilter


@admin.register(Category)
class GenreAdmin(admin.ModelAdmin):
    model = Category
    model_name="category"
    list_filter =(('children', TreeRelatedFieldListFilter),)
    mptt_level_indent = 20
    list_display=(
        'name',
        'parent',
        'action',
        
        # ...more fields if you feel like it...
    )
    def action(self, obj):
       return format_html('<a class="addlink" href="/admin/news/category/{}/change/">Edit</a>\
        <a class=" deletelink" href="/admin/news/category/{}/delete/">Delete</a>', obj.id,obj.id) 


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    model=NewsModel
    list_display=("name","action")
    
    def action(self, obj):
       return format_html(' <a class="addlink"  href="/admin/news/newsmodel/{}/change/">Edit</a>\
        <a class=" deletelink" href="/admin/news/newsmodel/{}/delete/">Delete</a>', obj.id,obj.id) 



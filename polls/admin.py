from django.contrib import admin

# Register your models here.

from .models import *
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)

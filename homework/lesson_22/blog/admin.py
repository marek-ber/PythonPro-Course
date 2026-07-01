from django.contrib import admin

from .models import Category, Post, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publication_date')
    list_filter = ('category', 'tags', 'publication_date')
    search_fields = ('title', 'content')
    filter_horizontal = ('tags',)
    ordering = ('-publication_date',)

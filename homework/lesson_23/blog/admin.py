from django.contrib import admin

from .models import Category, Post, Tag


admin.site.register(Category)
admin.site.register(Tag)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publication_date')
    list_filter = ('category', 'tags')
    search_fields = ('title', 'content')
    ordering = ('-publication_date',)

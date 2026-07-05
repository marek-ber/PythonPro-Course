from django.contrib import admin

from .models import Author, Book, Note, Product


admin.site.register(Product)
admin.site.register(Note)
admin.site.register(Author)
admin.site.register(Book)

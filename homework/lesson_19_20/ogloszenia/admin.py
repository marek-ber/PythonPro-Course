from django.contrib import admin

# Register your models here.

from .models import Ogloszenia 

# admin.site.register(Ogloszenia)
@admin.register(Ogloszenia)
class Ogloszenia(admin.ModelAdmin):
    list_display = ["title", "price", "created_add"]


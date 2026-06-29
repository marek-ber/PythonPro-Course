from django.contrib import admin

from .models import Note
# Register your models here.

# admin .site.register(Note)



# admin.site.register(Ogloszenia)
@admin.register(Note)
class Note(admin.ModelAdmin):
    list_display = ["title", "content"]
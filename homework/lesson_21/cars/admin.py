from django.contrib import admin
from .models import Car, Dealer
from django.utils.html import format_html


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('display_photo', 'full_name', 'brand', 'model', 'year', 'is_available')
    search_fields = ('brand', 'model')
    list_filter = ('year', 'is_available')
    ordering = ('year', )
    readonly_fields = ('year', )

    def get_readonly_fields(self, request, obj=None):
        if obj: # edycja istniejącego
            return ('year',)
        return () # przy dodawaniu nic nie blokuj

    def full_name(self, obj):
        return f"{obj.brand} {obj.model}"
    
    full_name.short_description = "Pełna nazwa"

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="150" />', obj.photo.url)
        else:
            return "Brak zdjęcia."

class CarInLine(admin.TabularInline):
    model = Car
    extra = 1

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    in_lines = [CarInLine]



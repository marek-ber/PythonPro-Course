from django.contrib import admin, messages
from django.utils.html import format_html

from .models import Car, Dealer


class CarInline(admin.TabularInline):
    model = Car
    extra = 1


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')
    inlines = [CarInline]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'brand',
        'model',
        'year',
        'is_available',
        'photo_thumbnail',
    )
    search_fields = ('brand', 'model')
    list_filter = ('is_available', 'year')
    ordering = ('-year',)
    actions = ('mark_as_unavailable',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('year',)
        return ()

    def full_name(self, obj):
        return f'{obj.brand} {obj.model}'

    full_name.short_description = 'Pełna nazwa'

    def photo_thumbnail(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="150" />',
                obj.photo.url,
            )
        return 'Brak zdjęcia'

    photo_thumbnail.short_description = 'Zdjęcie'

    def mark_as_unavailable(self, request, queryset):
        updated = queryset.update(is_available=False)

        self.message_user(
            request,
            f'Oznaczono jako niedostępne: {updated}',
            messages.SUCCESS,
        )

    mark_as_unavailable.short_description = 'Oznacz jako niedostępne'
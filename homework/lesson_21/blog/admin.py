from django.contrib import admin

from .models import Post, Category
from .ai_service import generate_text

# admin.site.register(Post)
# admin.site.register(Category)

class PostInLine(admin.TabularInline):
    model = Post
    
    extra = 1
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    
    inlines = [PostInLine]
    
    actions = ['make_published']

    def make_published(self, reguest, queryset):
        for category in queryset:
            print(category)
    
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    actions = ["generate_content", "translate_to_english", "suggest_tags"]

    def generate_content(self, request, queryset):
        for obj in queryset:
            prompt = f"Napisz angażujący artykuł na bloga o tytule: '{obj.title}'. Artykuł powinien mieć około 300 słów i być napisany w języku polskim."
            obj.content = generate_text(prompt)
            obj.save()

    generate_content.short_description = "Wygeneruj treść posta"

    def translate_to_english(self, request, queryset):
        for obj in queryset:
            prompt = f"Przetłumacz poniższy tekst na język angielski (styl formalny):\n\n{obj.content}"
            eng = generate_text(prompt)
            print(eng)
            obj.content = eng
            obj.save()

    translate_to_english.short_description = "Przetłumacz na angielski"

    def suggest_tags(self, request, queryset):
        for obj in queryset:
            prompt = f"Na podstawie tytułu '{obj.title}' i treści '{obj.content}', zasugeruj 5-7 tagów. Zwróć je jako lista oddzielona przecinkami."
            obj.tags = generate_text(prompt)
            obj.save()

    suggest_tags.short_description = "Zasugeruj tagi"
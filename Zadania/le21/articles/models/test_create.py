from . import Article

# Stworzenie nowego artykułu i zapisanie go w bazie danych
# To jest odpowiednik polecenia INSERT INTO w SQL
new_article = Article.objects.create(
    title="Nowy artykuł o Django",
    content="Treść artykułu o potędze ORM."
)

Article.objects.filter(title__contains="Django")

print(f"Utworzono artykuł o ID: {new_article.id}")




r"le21\articles\static\articles\styles.css"
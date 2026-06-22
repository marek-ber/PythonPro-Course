from django.shortcuts import render
from ..models import Article, ArticleForm


def article_list_view(request):
    # Pobieramy wszystkie artykuły z bazy

    all_articles = Article.objects.all().order_by(
        '-pub_date')  # sortujemy od najnowszych

    # Tworzymy "kontekst" - słownik danych do przekazania do szablonu
    context = {
        'articles': all_articles,
    }

    # Renderujemy szablon, przekazując obiekt request i kontekst
    return render(request, 'article_list.html', context)


def create_article(request):
    form = ArticleForm()

    return render(request, "form.html", {"form": form})

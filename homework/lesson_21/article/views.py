from django.http import HttpResponse
from django.shortcuts import render

from .models import Article, Category


def create_article(request):
    new_title = request.GET.get('title')
    new_content = request.GET.get('content')

    category = Category.objects.first()
    if category is None:
        category = Category.objects.create(name='Ogólne')

    new_article = Article.objects.create(
        title=new_title or 'Nowy artykuł',
        content=new_content or 'Brak treści',
        category=category,
    )

    return HttpResponse(f"Stworzono artykuł: {new_article.id}")


def filter_articles(request):
    query = request.GET.get('q')
    articles = Article.objects.filter(is_published=True).order_by('-pub_date')

    if query:
        articles = articles.filter(title__icontains=query)

    return render(
        request,
        'article/article_list.html',
        {
            'articles': articles,
            'query': query or '',
        },
    )


def view_categories(request):
    categories = Category.objects.all().order_by('name')
    return render(request, 'article/categories.html', {'categories': categories})


def category_detail_view(request, category_id):
    try:
        selected_category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        selected_category = None

    return render(
        request,
        'article/category_detail_view.html',
        {'category': selected_category},
    )


def category_detail(request, cat_id):
    try:
        category = Category.objects.get(id=cat_id)
        articles = category.article_set.filter(is_published=True).order_by('-pub_date')
    except Category.DoesNotExist:
        category = None
        articles = None

    return render(
        request,
        'article/category_detail.html',
        {
            'category': category,
            'articles': articles,
        },
    )

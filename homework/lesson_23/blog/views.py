from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Category, Post


def post_list(request):
    query = request.GET.get('q', '')
    posts = Post.objects.all()

    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    else:
        posts = posts.order_by('-publication_date')[:5]

    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'query': query,
    })


def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category).order_by('-publication_date')

    return render(request, 'blog/category_posts.html', {
        'category': category,
        'posts': posts,
    })

from django.urls import path
from .views.article_view import create_article, article_list_view

urlpatterns = [
    path('', article_list_view, name="article-list"),
    path("create/", create_article, name="article-create"),
]


# 
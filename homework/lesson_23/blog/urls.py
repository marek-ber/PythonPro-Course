from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='blog-home'),
    path('category/<int:category_id>/', views.category_posts, name='category-posts'),
]

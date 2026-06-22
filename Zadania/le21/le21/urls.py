"""
URL configuration for le21 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from articles.views.article_view import article_list_view
from articles.views.static_test_view import static_view
from articles.views.article_view import create_article

urlpatterns = [
    path('admin/', admin.site.urls),
    path('static-test/', static_view, name='static-test'),
    path('articles/', include('articles.urls'))
]

"""
URL configuration for mojprojekt project.

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
from django.urls import path
from ogloszenia.views import hello_world, show_product
from ogloszenia.views import hello_world, show_product, HelloWorld2, show_ogloszenia
from blog.views import home_view, contact_view, info, rules, greet_user
from product.views import show_product, ShowProducts, add_product
from notatnik.views import all_notes, one_note

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', hello_world),
    path('product/<int:product_id>/', show_product, name='product-details'),
    path('home/', home_view, name='home-view'),
    path('contact/', contact_view),
    path('ogloszenia/', show_ogloszenia),
    path('info/', info),
    path('rules/', rules),
    path('user/<str:username>', greet_user),
    path('products/', show_product, name='products'),
    path('products2/', ShowProducts.as_view()),
    path('notes/', all_notes),
    path('notes/<int:note_id>/', one_note),
    path('add-products/', add_product, name='add-products')
]

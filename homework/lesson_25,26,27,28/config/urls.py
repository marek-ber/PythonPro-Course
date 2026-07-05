from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from api import views

router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='product')
router.register('cached-products', views.CachedProductViewSet, basename='cached-product')
router.register('notes', views.NoteViewSet, basename='note')
router.register('authors', views.AuthorViewSet, basename='author')
router.register('books', views.BookViewSet, basename='book')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    path('api/hello/', views.hello, name='hello'),
    path('api/set-name/', views.set_name, name='set-name'),
    path('api/calculate/', views.calculate, name='calculate'),
    path('api/profile/', views.profile_api, name='profile-api'),
    path('api/products-cached-list/', views.cached_products_list, name='cached-products-list'),
    path('api/complex-cache/', views.complex_cache_view, name='complex-cache'),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/schema/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

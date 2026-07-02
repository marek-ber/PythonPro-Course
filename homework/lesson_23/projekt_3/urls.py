from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from products.views import all_products, home, register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('home/', home, name='home'),
    path('products/', all_products, name='products'),
    path('blog/', include('blog.urls')),
    path(
        'change_password/',
        auth_views.PasswordChangeView.as_view(template_name='users/change_password.html'),
        name='change-password',
    ),
    path(
        'password_change_done/',
        auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
        name='password_change_done',
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

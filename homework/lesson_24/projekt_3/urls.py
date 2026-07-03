from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from products.views import (
    all_products,
    home,
    next_info,
    profile,
    register,
    staff_users,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('register/', register, name='register'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='users/login.html'),
        name='login',
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='users/logout.html'),
        name='logout',
    ),
    path('profile/', profile, name='profile'),
    path('products/', all_products, name='products'),
    path('staff/users/', staff_users, name='staff-users'),
    path('next-info/', next_info, name='next-info'),
    path(
        'password-change/',
        auth_views.PasswordChangeView.as_view(
            template_name='users/password_change_form.html',
            success_url='/password-change-done/',
        ),
        name='password-change',
    ),
    path(
        'password-change-done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html',
        ),
        name='password-change-done',
    ),
]

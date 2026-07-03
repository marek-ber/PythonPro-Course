from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm
from .models import Product


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Konto zostało utworzone. Jesteś zalogowany.')
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/all.html', {'products': products})


@staff_member_required
def staff_users(request):
    users = User.objects.all()
    return render(request, 'users/staff_users.html', {'users': users})


def next_info(request):
    return render(request, 'users/next_info.html')

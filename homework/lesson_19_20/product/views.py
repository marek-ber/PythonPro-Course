from django.shortcuts import render, redirect
from .models import Product
from django.views import View
from .forms import ProductForm

# Create your views here.

def show_product(request):
    all_products = Product.objects.all()
    return render(request, 'products.html', {"products": all_products})

class ShowProducts(View):
    def show_product(request):
        all_products = Product.objects.all()
        return render(request, 'products.html', {"products": all_products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'])                    
            return redirect('products')
        
    else:
            # Jeśli to zapytanie GET, tworzymy pusty formularz
        form = ProductForm()
        return render(request, 'add_products.html', {'form': form})
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.

def home_view(request):
    # Przygotowujemy dane, które chcemy przekazać do szablonu
    context = {
    'user_name': 'Anna',
    'products': [
            {'name': 'Jabłka', 'price': 3.50},
            {'name': 'Banany', 'price': 5.99},
            {'name': 'Truskawki', 'price': 12.00},
        ]
    }
  
    return render(request, 'home.html', context)


def contact_view(request):
    if request.method == 'POST':
    # Jeśli formularz został wysłany, tworzymy instancję z danymi POST
        form = ContactForm(request.POST)
        if form.is_valid():
        # Jeśli dane są poprawne, możemy je przetworzyć
            name = form.cleaned_data['name']
            print(f"Otrzymano wiadomość od: {name}")
        
            return redirect('home-view') # 'success-page' to nazwa URL
        else:
            return render(request, 'contact.html', {'form': form, 'error': "Nieprawidłowe dane"})
    else:
            # Jeśli to zapytanie GET, tworzymy pusty formularz
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})
    
def info(request):
    return HttpResponse("Informacje o stronie")

def rules(request):
    return HttpResponse("Regulamin")

def greet_user(request, username):
    return HttpResponse(f"Witaj na profilu, {username}")
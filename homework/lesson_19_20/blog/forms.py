from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Twoje imię', max_length=10)
    email = forms.EmailField(label='Twój email')
    message = forms.CharField(label='Wiadomość', widget=forms.Textarea)
    age = forms.IntegerField(min_value=0)
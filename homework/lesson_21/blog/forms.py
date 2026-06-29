from django import forms

class SearchForm(forms.Form):
    phrase = forms.CharField(max_length=100)
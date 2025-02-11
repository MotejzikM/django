from django import forms
from .models import Obraz

class ObrazForm(forms.ModelForm):
    class Meta:
        model = Obraz
        fields = ["nazev", "autor", "rok", "technika", "cena", "poznamky", "img"]
from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["jmeno", "narozen", "umrti", "zivotopis", "img"]
        # nastavení typu inputu
        widgets = {
            'narozen': forms.DateInput(attrs={'type': 'date'}),
            'umrti': forms.DateInput(attrs={'type': 'date'}),
        }
from django import forms
from .models import Salles

class SallesForm(forms.ModelForm):
    class Meta:
        model = Salles
        fields = ['nom', 'capacite', 'prise']

class ExcelUploadForm(forms.Form):
    file = forms.FileField(required=False)
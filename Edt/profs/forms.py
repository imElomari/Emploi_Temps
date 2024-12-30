from django import forms
from .models import Professeurs

class ProfsForm(forms.ModelForm):
    class Meta:
        model = Professeurs
        fields = ['ISBN', 'nom', 'prenom', 'nbr_heur_semaine']

class ExcelUploadForm(forms.Form):
    file = forms.FileField(required=False)
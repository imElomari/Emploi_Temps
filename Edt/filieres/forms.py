from django import forms
from django.contrib.contenttypes.models import ContentType

from filieres.models import Filieres, TDs, Modules
from profs.models import Professeurs


class FilieresForm(forms.ModelForm):
    class Meta:
        model = Filieres
        fields = ['code', 'nom', 'effectif']

class TdsForm(forms.ModelForm):
    class Meta:
        model = TDs
        fields = ['nom', 'effectif']

class ModulesForm(forms.ModelForm):
    professeurs = forms.ModelMultipleChoiceField(
        queryset=Professeurs.objects.all(),
        widget=forms.SelectMultiple,
        required=True
    )

    class Meta:
        model = Modules
        fields = ['nom', 'professeurs', 'nbr_heurs', 'nbr_semaines']

    def clean_professeurs(self):
        professeurs = self.cleaned_data.get('professeurs')
        if not (1 <= len(professeurs) <= 2):
            raise forms.ValidationError("You must select one or two professors.")
        return professeurs

class ExcelUploadForm(forms.Form):
    file = forms.FileField(required=False)
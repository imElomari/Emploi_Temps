import pandas as pd
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View

from .forms import SallesForm, ExcelUploadForm
from .models import Salles

class SallesCreateView(View):
    template_name = 'create_module.html'
    success_url = reverse_lazy('list_salles')

    def get(self, request):
        salles_form = SallesForm()
        excel_form = ExcelUploadForm()
        return render(request, self.template_name, {'salles_form': salles_form, 'excel_form': excel_form})

    def post(self, request):
        salles_form = SallesForm(request.POST)
        excel_form = ExcelUploadForm(request.POST, request.FILES)

        if 'save_salle' in request.POST and salles_form.is_valid():
            salles_form.save()
            return redirect(self.success_url)

        if 'upload_excel' in request.POST and excel_form.is_valid():
            excel_file = request.FILES['file']
            df = pd.read_excel(excel_file, engine='openpyxl')
            for _, row in df.iterrows():
                Salles.objects.create(
                    nom=row['Nom'],
                    capacite=row['Capacite'],
                    prise=row['Prise']
                )
            return redirect(self.success_url)

        return render(request, self.template_name, {'salles_form': salles_form, 'excel_form': excel_form})
class SallesListView(ListView):
    model = Salles
    template_name = 'list_salles.html'
    context_object_name = 'salles'

class SallesUpdateView(UpdateView):
    model = Salles
    form_class = SallesForm
    template_name = 'update_salle.html'
    success_url = reverse_lazy('list_salles')

class SallesDeleteView(DeleteView):
    model = Salles
    template_name = 'delete_salle.html'
    success_url = reverse_lazy('list_salles')

class ExcelUploadView(View):
    template_name = 'upload_excel.html'
    success_url = reverse_lazy('list_salles')

    def get(self, request):
        form = ExcelUploadForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            df = pd.read_excel(excel_file)
            for _, row in df.iterrows():
                Salles.objects.create(
                    nom=row['nom'],
                    capacite=row['capacite'],
                    prise=row['prise']
                )
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})

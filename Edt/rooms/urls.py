from django.urls import path

from rooms.views import SallesListView, SallesCreateView, SallesUpdateView, SallesDeleteView, ExcelUploadView

urlpatterns = [
    path('',SallesListView.as_view(), name='list_salles'),
    path('create/', SallesCreateView.as_view(), name='create_salle'),
    path('update/<int:pk>/', SallesUpdateView.as_view(), name='update_salle'),
    path('delete/<int:pk>/', SallesDeleteView.as_view(), name='delete_salle'),


]
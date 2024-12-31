from django.urls import path

from profs.views import ProfsListView, ProfsCreateView, ProfsUpdateView, ProfsDeleteView

app_name = 'profs'

urlpatterns = [
    path('', ProfsListView.as_view(), name='list_profs'),
    path('create/', ProfsCreateView.as_view(), name='create_prof'),
    path('update/<int:pk>/', ProfsUpdateView.as_view(), name='update_prof'),
    path('delete/<int:pk>/', ProfsDeleteView.as_view(), name='delete_prof'),


]
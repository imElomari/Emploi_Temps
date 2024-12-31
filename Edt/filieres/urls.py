from django.urls import path

from filieres.views import FilieresListView, FilieresCreateView, FilieresUpdateView, FilieresDeleteView, TdsListView, \
    TdsCreateView, TdsUpdateView, TdsDeleteView, ModulesListView, ModulesCreateView, ModulesUpdateView, \
    ModulesDeleteView

urlpatterns = [
    path('',FilieresListView.as_view(), name='list_filieres'),
    path('create/', FilieresCreateView.as_view(), name='create_filiere'),
    path('update/<int:pk>/', FilieresUpdateView.as_view(), name='update_filiere'),
    path('delete/<int:pk>/', FilieresDeleteView.as_view(), name='delete_filiere'),
    path('tds/',TdsListView.as_view(), name='list_tds'),
    path('createTd/', TdsCreateView.as_view(), name='create_td'),
    path('updateTd/<int:pk>/', TdsUpdateView.as_view(), name='update_td'),
    path('deleteTd/<int:pk>/', TdsDeleteView.as_view(), name='delete_td'),
    #path('modules/',ModulesListView.as_view(), name='list_modules'),
    path('modules/filiere/<int:filiere_id>/', ModulesListView.as_view(), name='list_modules_filiere'),
    path('modules/td/<int:td_id>/', ModulesListView.as_view(), name='list_modules_td'),

    path('modules/create/<int:filiere_id>/', ModulesCreateView.as_view(), name='create_module_filiere'),
    path('modules/create/td/<int:td_id>/', ModulesCreateView.as_view(), name='create_module_td'),
    path('updateModule/<int:pk>/', ModulesUpdateView.as_view(), name='update_module'),
    path('modules/delete/<int:pk>/', ModulesDeleteView.as_view(), name='delete_module'),


]
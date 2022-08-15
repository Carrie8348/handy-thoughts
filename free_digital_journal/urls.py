from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_free_downloads, name='all_free_downloads'),
    path('<int:free_download_id>/', views.free_dowonlad_detail, name='free_dowonlad_detail'),
    path('add_free_download/', views.add_free_download, name='add_free_download'),
    path('edit_free_dowonload/<int:free_download_id>/', views.edit_free_download, name='edit_free_download'),
    path('delete_free_download/<int:free_download_id>/', views.delete_free_download, name='delete_free_download'),
]
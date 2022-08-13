from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_file, name='view_file'),
    path('<int:file_id>/', views.file_detail, name='file_detail'),
    path('add_file/', views.add_file, name='add_file'),
    path('edit_file/<int:file_id>/', views.edit_file, name='edit_file'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),
]
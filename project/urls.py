from django.urls import path, include
from . import views


app_name="project"

urlpatterns = [
    path('', views.projects, name="projects"),
    path('add/', views.add_project, name="add"),
    path('<uuid:pk>/', views.project, name="project"),
    path('<uuid:pk>/edit/', views.edit_porject, name="edit"),
    path('<uuid:pk>/delete/', views.delete_project, name="delete"),
    path('<uuid:project_id>/upload_file/', views.upload_file, name="upload_file"),
    path('<uuid:project_id>/<uuid:pk>/delete/', views.delete_upload, name="delete"),
    path('<uuid:project_id>/add_note/', views.create_note, name="add_note"),
    path('<uuid:project_id>/<uuid:pk>/note_detail/', views.note_detail, name="note_detail"),
    path('<uuid:project_id>/<uuid:pk>/edit_note/', views.edit_note, name="edit_note"),
    path('<uuid:project_id>/<uuid:pk>/note_delete/', views.note_delete, name="note_delete"),
]
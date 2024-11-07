from django.urls import path, include
from . import views

app_name = 'todolist'


urlpatterns =  [
    path('add/', views.add, name='add'),
    path('<uuid:pk>/', views.todoList, name='todolist'),
    path('<uuid:pk>/edit/', views.edit, name='edit'),
    path('<uuid:pk>/delete/', views.delete, name='delete'),
]
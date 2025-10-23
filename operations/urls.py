from django.urls import path
from . import views

urlpatterns = [
    path('', views.operation_list, name='operation_list'),
    path('add/', views.operation_add, name='operation_add'),
    path('<int:id>/edit/', views.operation_edit, name='operation_edit'),
    path('<int:id>/delete/', views.operation_delete, name='operation_delete'),
]


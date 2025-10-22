from django.urls import path
from . import views

urlpatterns = [
    path('', views.sales_list, name='sales_list'),
    path('add/', views.sales_add, name='sales_add'),
    path('<int:id>/edit/', views.sales_edit, name='sales_edit'),
    path('<int:id>/delete/', views.sales_delete, name='sales_delete'),
]

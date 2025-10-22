from django.urls import path
from . import views
from reports import views as report_views  # for field-specific report links

urlpatterns = [
    path('', views.field_list, name='field_list'),
    path('add/', views.field_add, name='field_add'),
    path('<int:id>/edit/', views.field_edit, name='field_edit'),
    path('<int:id>/delete/', views.field_delete, name='field_delete'),
    path('<int:id>/report/', report_views.field_report, name='field_report'),
]

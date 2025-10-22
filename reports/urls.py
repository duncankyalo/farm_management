from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_dashboard, name='report_dashboard'),
    path('field/<int:id>/', views.field_report, name='field_report'),
]

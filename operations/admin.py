from django.contrib import admin
from .models import Operation

@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ('operation_type', 'field', 'date', 'worker_name', 'hours_spent')
    search_fields = ('operation_type', 'field__name', 'worker_name')
    list_filter = ('operation_type', 'date')

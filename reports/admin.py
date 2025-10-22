from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('field', 'total_sales', 'total_expenses', 'profit_or_loss', 'last_updated')
    search_fields = ('field__name',)
    readonly_fields = ('total_sales', 'total_expenses', 'profit_or_loss', 'last_updated')

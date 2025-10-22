from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('category', 'field', 'amount', 'date', 'description')
    search_fields = ('category', 'field__name', 'description')
    list_filter = ('category', 'date')

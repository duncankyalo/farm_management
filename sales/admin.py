from django.contrib import admin
from .models import Sale

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('produce_name', 'field', 'quantity', 'unit_price', 'date', 'total_amount')
    search_fields = ('produce_name', 'field__name')
    list_filter = ('date',)

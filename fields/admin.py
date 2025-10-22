from django.contrib import admin
from .models import Field

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'size_acres', 'crop_type', 'location', 'date_planted')
    search_fields = ('name', 'crop_type', 'location')
    list_filter = ('crop_type',)

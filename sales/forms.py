from django import forms
from .models import Sale

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['field', 'date', 'quantity', 'price_per_unit', 'buyer']

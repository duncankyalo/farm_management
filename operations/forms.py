from django import forms
from .models import Operation

class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['field', 'operation_type', 'date', 'cost', 'notes']

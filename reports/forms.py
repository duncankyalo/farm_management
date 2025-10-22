from django import forms
from django.forms import DateInput

class ReportFilterForm(forms.Form):
    start_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

from django.db import models
from fields.models import Field

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Labor', 'Labor'),
        ('Fertilizer', 'Fertilizer'),
        ('Seeds', 'Seeds'),
        ('Fuel', 'Fuel'),
        ('Machinery Repair', 'Machinery Repair'),
        ('Power', 'Power'),
        ('Misc', 'Miscellaneous'),
    ]

    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='expenses')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200, blank=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.category} - {self.amount}"

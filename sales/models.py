from django.db import models
from fields.models import Field

class Sale(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='sales')
    produce_name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def total_amount(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.produce_name} - {self.field.name}"

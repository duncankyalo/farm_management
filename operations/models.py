from django.db import models
from fields.models import Field

class Operation(models.Model):
    OPERATION_TYPES = [
        ('Planting', 'Planting'),
        ('Weeding', 'Weeding'),
        ('Fertilizing', 'Fertilizing'),
        ('Irrigation', 'Irrigation'),
        ('Harvesting', 'Harvesting'),
        ('Spraying', 'Spraying'),
    ]

    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='operations')
    operation_type = models.CharField(max_length=50, choices=OPERATION_TYPES)
    date = models.DateField()
    worker_name = models.CharField(max_length=100, blank=True)
    hours_spent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.operation_type} - {self.field.name}"

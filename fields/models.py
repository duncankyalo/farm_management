from django.db import models

class Field(models.Model):
    name = models.CharField(max_length=100)
    size_acres = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.CharField(max_length=200, blank=True)
    crop_type = models.CharField(max_length=100)
    date_planted = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

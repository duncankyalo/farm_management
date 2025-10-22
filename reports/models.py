from django.db import models
from fields.models import Field
from expenses.models import Expense
from sales.models import Sale

class Report(models.Model):
    field = models.OneToOneField(Field, on_delete=models.CASCADE, related_name='report')
    total_expenses = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_sales = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    profit_or_loss = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def update_financials(self):
        total_exp = sum(e.amount for e in Expense.objects.filter(field=self.field))
        total_rev = sum(s.total_amount() for s in Sale.objects.filter(field=self.field))
        self.total_expenses = total_exp
        self.total_sales = total_rev
        self.profit_or_loss = total_rev - total_exp
        self.save()

    def __str__(self):
        return f"Report for {self.field.name}"

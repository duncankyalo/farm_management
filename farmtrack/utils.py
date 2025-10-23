from django.db.models import Sum, F
from expenses.models import Expense
from sales.models import Sale
from fields.models import Field

def calculate_total_expenses(start_date=None, end_date=None):
    qs = Expense.objects.all()
    if start_date and end_date:
        qs = qs.filter(date__range=[start_date, end_date])
    return qs.aggregate(total=Sum('amount'))['total'] or 0

def calculate_total_sales(start_date=None, end_date=None):
    qs = Sale.objects.all()
    if start_date and end_date:
        qs = qs.filter(date__range=[start_date, end_date])
    return qs.aggregate(total=Sum(F('quantity') * F('unit_price')))['total'] or 0

def calculate_profit(start_date=None, end_date=None):
    return calculate_total_sales(start_date, end_date) - calculate_total_expenses(start_date, end_date)

def generate_financial_summary(start_date=None, end_date=None):
    """Return summary data including per-field totals."""
    total_sales = calculate_total_sales(start_date, end_date)
    total_expenses = calculate_total_expenses(start_date, end_date)
    profit = total_sales - total_expenses

    # Per-field breakdown
    field_summaries = []
    for field in Field.objects.all():
        field_expenses = Expense.objects.filter(field=field)
        field_sales = Sale.objects.filter(field=field)

        if start_date and end_date:
            field_expenses = field_expenses.filter(date__range=[start_date, end_date])
            field_sales = field_sales.filter(date__range=[start_date, end_date])

        total_exp = field_expenses.aggregate(total=Sum('amount'))['total'] or 0
        total_rev = field_sales.aggregate(total=Sum(F('quantity') * F('unit_price')))['total'] or 0
        profit_or_loss = total_rev - total_exp

        field_summaries.append({
            'field': field.name,
            'total_expenses': total_exp,
            'total_sales': total_rev,
            'profit_or_loss': profit_or_loss
        })

    summary = {
        'total_sales': total_sales,
        'total_expenses': total_expenses,
        'profit': profit,
        'status': 'Profit' if profit >= 0 else 'Loss',
        'fields': field_summaries
    }
    return summary

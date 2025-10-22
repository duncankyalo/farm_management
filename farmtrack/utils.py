from django.db.models import Sum, F
from expenses.models import Expense
from sales.models import Sale

def calculate_total_expenses(start_date=None, end_date=None):
    """Compute total farm expenses in a given date range."""
    qs = Expense.objects.all()
    if start_date and end_date:
        qs = qs.filter(date__range=[start_date, end_date])
    total = qs.aggregate(total=Sum('amount'))['total'] or 0
    return total

def calculate_total_sales(start_date=None, end_date=None):
    """Compute total sales revenue in a given date range."""
    qs = Sale.objects.all()
    if start_date and end_date:
        qs = qs.filter(date__range=[start_date, end_date])
    total = qs.aggregate(
        total=Sum(F('quantity') * F('price_per_unit'))
    )['total'] or 0
    return total

def calculate_profit(start_date=None, end_date=None):
    """Compute profit or loss for the period."""
    total_sales = calculate_total_sales(start_date, end_date)
    total_expenses = calculate_total_expenses(start_date, end_date)
    return total_sales - total_expenses

def generate_financial_summary(start_date=None, end_date=None):
    """Return summary data for dashboard or report views."""
    total_sales = calculate_total_sales(start_date, end_date)
    total_expenses = calculate_total_expenses(start_date, end_date)
    profit = total_sales - total_expenses

    summary = {
        'total_sales': total_sales,
        'total_expenses': total_expenses,
        'profit': profit,
        'status': 'Profit' if profit >= 0 else 'Loss'
    }
    return summary

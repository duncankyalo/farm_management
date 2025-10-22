from django.shortcuts import render, get_object_or_404
from fields.models import Field
from expenses.models import Expense
from sales.models import Sale
from .forms import ReportFilterForm
from farmtrack.utils import generate_financial_summary

def report_dashboard(request):
    form = ReportFilterForm(request.GET or None)

    if form.is_valid():
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        summary = generate_financial_summary(start_date, end_date)
    else:
        start_date = None
        end_date = None
        summary = generate_financial_summary()

    reports = []
    fields = Field.objects.all()

    for field in fields:
        expenses_qs = Expense.objects.filter(field=field)
        sales_qs = Sale.objects.filter(field=field)

        if start_date and end_date:
            expenses_qs = expenses_qs.filter(date__range=[start_date, end_date])
            sales_qs = sales_qs.filter(date__range=[start_date, end_date])

        total_exp = sum(e.amount for e in expenses_qs)
        total_rev = sum(s.total_amount() for s in sales_qs)
        profit = total_rev - total_exp

        reports.append({
            'field': field.name,
            'total_expenses': total_exp,
            'total_sales': total_rev,
            'profit_or_loss': profit
        })

    context = {
        'form': form,
        'summary': summary,
        'reports': reports,
    }
    return render(request, 'reports/report_dashboard.html', context)


def field_report(request, id):
    field = get_object_or_404(Field, id=id)
    expenses = Expense.objects.filter(field=field)
    sales = Sale.objects.filter(field=field)

    total_exp = sum(e.amount for e in expenses)
    total_rev = sum(s.total_amount() for s in sales)
    profit = total_rev - total_exp

    return render(request, 'reports/field_report.html', {
        'field': field,
        'expenses': expenses,
        'sales': sales,
        'total_expenses': total_exp,
        'total_sales': total_rev,
        'profit_or_loss': profit,
    })

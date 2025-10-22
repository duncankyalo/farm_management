from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from fields.models import Field
from django.contrib import messages

def expense_list(request):
    expenses = Expense.objects.select_related('field').all()
    total_expenses = sum(e.amount for e in expenses)
    return render(request, 'expenses/expense_list.html', {'expenses': expenses, 'total_expenses': total_expenses})

def expense_add(request):
    fields = Field.objects.all()
    if request.method == 'POST':
        Expense.objects.create(
            field_id=request.POST['field'],
            category=request.POST['category'],
            amount=request.POST['amount'],
            description=request.POST.get('description', ''),
            date=request.POST['date']
        )
        messages.success(request, 'Expense recorded')
        return redirect('expense_list')
    return render(request, 'expenses/expense_add.html', {'fields': fields})

def expense_edit(request, id):
    expense = get_object_or_404(Expense, id=id)
    fields = Field.objects.all()
    if request.method == 'POST':
        expense.field_id = request.POST['field']
        expense.category = request.POST['category']
        expense.amount = request.POST['amount']
        expense.description = request.POST.get('description', '')
        expense.date = request.POST['date']
        expense.save()
        messages.success(request, 'Expense updated')
        return redirect('expense_list')
    return render(request, 'expenses/expense_edit.html', {'expense': expense, 'fields': fields})

def expense_delete(request, id):
    expense = get_object_or_404(Expense, id=id)
    expense.delete()
    messages.info(request, 'Expense deleted')
    return redirect('expense_list')

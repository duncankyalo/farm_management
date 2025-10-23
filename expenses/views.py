from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from fields.models import Field
from django.contrib import messages

def expense_list(request):
    expenses = Expense.objects.select_related('field').all()
    total_expenses = sum(e.amount for e in expenses)
    return render(request, 'expenses/expense_list.html', {
        'expenses': expenses,
        'total_expenses': total_expenses
    })

def expense_add(request):
    fields = Field.objects.all()
    if request.method == 'POST':
        field_id = request.POST.get('field')
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        description = request.POST.get('description', '')

        if field_id and category and amount and date:
            Expense.objects.create(
                field_id=field_id,
                category=category,
                amount=amount,
                date=date,
                description=description
            )
            messages.success(request, 'Expense recorded')
            return redirect('expense_list')
        else:
            messages.error(request, 'Please fill in all required fields')

    return render(request, 'expenses/expense_add.html', {'fields': fields})

def expense_edit(request, id):
    expense = get_object_or_404(Expense, id=id)
    fields = Field.objects.all()
    if request.method == 'POST':
        field_id = request.POST.get('field')
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        description = request.POST.get('description', '')

        if field_id and category and amount and date:
            expense.field_id = field_id
            expense.category = category
            expense.amount = amount
            expense.date = date
            expense.description = description
            expense.save()
            messages.success(request, 'Expense updated')
            return redirect('expense_list')
        else:
            messages.error(request, 'Please fill in all required fields')

    return render(request, 'expenses/expense_edit.html', {
        'expense': expense,
        'fields': fields
    })

def expense_delete(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == 'POST':
        expense.delete()
        messages.info(request, 'Expense deleted')
        return redirect('expense_list')

    return render(request, 'expenses/expense_delete.html', {'expense': expense})

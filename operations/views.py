from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Operation
from fields.models import Field

def operation_list(request):
    operations = Operation.objects.select_related('field').all().order_by('-date')
    return render(request, 'operations/operation_list.html', {'operations': operations})

def operation_add(request):
    fields = Field.objects.all()
    if request.method == 'POST':
        field_id = request.POST.get('field')
        operation_type = request.POST.get('operation_type', '').strip()
        date_input = request.POST.get('date')
        worker_name = request.POST.get('worker_name', '').strip()
        hours_spent = request.POST.get('hours_spent', 0)
        cost = request.POST.get('cost', 0)
        notes = request.POST.get('notes', '').strip()

        if not field_id or not operation_type or not date_input:
            messages.error(request, 'Field, operation type, and date are required.')
            return redirect('operation_add')

        # Convert numeric inputs safely
        try:
            hours_spent = float(hours_spent)
        except ValueError:
            hours_spent = 0

        try:
            cost = float(cost)
        except ValueError:
            cost = 0

        Operation.objects.create(
            field_id=field_id,
            operation_type=operation_type,
            date=date_input,
            worker_name=worker_name,
            hours_spent=hours_spent,
            cost=cost,
            notes=notes
        )

        messages.success(request, 'Operation recorded successfully')
        return redirect('operation_list')

    return render(request, 'operations/operation_add.html', {'fields': fields})

def operation_edit(request, id):
    operation = get_object_or_404(Operation, id=id)
    fields = Field.objects.all()
    if request.method == 'POST':
        field_id = request.POST.get('field')
        operation_type = request.POST.get('operation_type', '').strip()
        date_input = request.POST.get('date')
        worker_name = request.POST.get('worker_name', '').strip()
        notes = request.POST.get('notes', '').strip()

        if not field_id or not operation_type or not date_input:
            messages.error(request, 'Field, operation type, and date are required.')
            return redirect('operation_edit', id=id)

        operation.field_id = field_id
        operation.operation_type = operation_type
        operation.date = date_input

        try:
            operation.hours_spent = float(request.POST.get('hours_spent', 0))
        except ValueError:
            operation.hours_spent = 0

        try:
            operation.cost = float(request.POST.get('cost', 0))
        except ValueError:
            operation.cost = 0

        operation.worker_name = worker_name
        operation.notes = notes

        operation.save()
        messages.success(request, 'Operation updated successfully')
        return redirect('operation_list')

    return render(request, 'operations/operation_edit.html', {'operation': operation, 'fields': fields})

def operation_delete(request, id):
    operation = get_object_or_404(Operation, id=id)
    operation.delete()
    messages.info(request, 'Operation deleted')
    return redirect('operation_list')

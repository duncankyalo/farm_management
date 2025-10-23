from django.shortcuts import render, redirect, get_object_or_404
from .models import Operation
from fields.models import Field
from django.contrib import messages

def operation_list(request):
    operations = Operation.objects.select_related('field').all().order_by('-date')
    return render(request, 'operations/operation_list.html', {'operations': operations})

def operation_add(request):
    fields = Field.objects.all()
    if request.method == 'POST':
        field_id = request.POST['field']
        Operation.objects.create(
            field_id=field_id,
            operation_type=request.POST['operation_type'],
            date=request.POST['date'],
            worker_name=request.POST.get('worker_name', ''),
            hours_spent=request.POST.get('hours_spent', 0),
            notes=request.POST.get('notes', '')
        )
        messages.success(request, 'Operation recorded successfully')
        return redirect('operation_list')
    return render(request, 'operations/operation_add.html', {'fields': fields})

def operation_edit(request, id):
    operation = get_object_or_404(Operation, id=id)
    fields = Field.objects.all()
    if request.method == 'POST':
        operation.field_id = request.POST['field']
        operation.operation_type = request.POST['operation_type']
        operation.date = request.POST['date']
        operation.worker_name = request.POST.get('worker_name', '')
        operation.hours_spent = request.POST.get('hours_spent', 0)
        operation.notes = request.POST.get('notes', '')
        operation.save()
        messages.success(request, 'Operation updated')
        return redirect('operation_list')
    return render(request, 'operations/operation_edit.html', {'operation': operation, 'fields': fields})

def operation_delete(request, id):
    operation = get_object_or_404(Operation, id=id)
    operation.delete()
    messages.info(request, 'Operation deleted')
    return redirect('operation_list')

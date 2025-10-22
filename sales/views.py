from django.shortcuts import render, redirect, get_object_or_404
from .models import Sale
from fields.models import Field
from django.contrib import messages

def sales_list(request):
    sales = Sale.objects.select_related('field').all()
    total_revenue = sum(s.total_amount() for s in sales)
    return render(request, 'sales/sales_list.html', {'sales': sales, 'total_revenue': total_revenue})

def sales_add(request):
    fields = Field.objects.all()
    if request.method == 'POST':
        Sale.objects.create(
            field_id=request.POST['field'],
            produce_name=request.POST['produce_name'],
            quantity=request.POST['quantity'],
            unit_price=request.POST['unit_price'],
            date=request.POST['date']
        )
        messages.success(request, 'Sale added')
        return redirect('sales_list')
    return render(request, 'sales/sales_add.html', {'fields': fields})

def sales_edit(request, id):
    sale = get_object_or_404(Sale, id=id)
    fields = Field.objects.all()
    if request.method == 'POST':
        sale.field_id = request.POST['field']
        sale.produce_name = request.POST['produce_name']
        sale.quantity = request.POST['quantity']
        sale.unit_price = request.POST['unit_price']
        sale.date = request.POST['date']
        sale.save()
        messages.success(request, 'Sale updated')
        return redirect('sales_list')
    return render(request, 'sales/sales_edit.html', {'sale': sale, 'fields': fields})

def sales_delete(request, id):
    sale = get_object_or_404(Sale, id=id)
    sale.delete()
    messages.info(request, 'Sale deleted')
    return redirect('sales_list')

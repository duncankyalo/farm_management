from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Field


def field_list(request):
    """Display all fields with links to individual reports."""
    fields = Field.objects.all().order_by('name')
    return render(request, 'fields/field_list.html', {'fields': fields})


def field_add(request):
    """Add a new field record."""
    if request.method == 'POST':
        name = request.POST.get('name')
        size_acres = request.POST.get('size_acres')
        location = request.POST.get('location')
        crop_type = request.POST.get('crop_type')
        date_planted = request.POST.get('date_planted')

        if not name or not size_acres or not crop_type:
            messages.error(request, 'Name, size, and crop type are required.')
            return redirect('field_add')

        Field.objects.create(
            name=name.strip(),
            size_acres=size_acres,
            location=location or '',
            crop_type=crop_type.strip(),
            date_planted=date_planted or None
        )

        messages.success(request, 'Field added successfully.')
        return redirect('field_list')

    return render(request, 'fields/field_add.html')


def field_edit(request, id):
    """Edit existing field details."""
    field = get_object_or_404(Field, id=id)

    if request.method == 'POST':
        field.name = request.POST.get('name')
        field.size_acres = request.POST.get('size_acres')
        field.location = request.POST.get('location')
        field.crop_type = request.POST.get('crop_type')
        field.date_planted = request.POST.get('date_planted')
        field.save()

        messages.success(request, 'Field updated successfully.')
        return redirect('field_list')

    return render(request, 'fields/field_edit.html', {'field': field})


def field_delete(request, id):
    """Delete a field."""
    field = get_object_or_404(Field, id=id)
    field.delete()
    messages.info(request, 'Field deleted successfully.')
    return redirect('field_list')


def field_report(request, id):
    """Display detailed report for a specific field."""
    field = get_object_or_404(Field, id=id)

    # Example data aggregation (adjust based on your models)
    expenses = Expense.objects.filter(field=field)
    yields = Yield.objects.filter(field=field)
    weather = Weather.objects.filter(field=field)

    total_expenses = sum(e.amount for e in expenses)
    total_yield = sum(y.amount for y in yields)
    profit = total_yield - total_expenses

    context = {
        'field': field,
        'expenses': expenses,
        'yields': yields,
        'weather': weather,
        'total_expenses': total_expenses,
        'total_yield': total_yield,
        'profit': profit,
    }

    return render(request, 'fields/field_report.html', context)

from django.shortcuts import render

def home(request):
    modules = [
        {'name': 'Fields', 'url': '/fields/'},
        {'name': 'Operations', 'url': '/operations/'},
        {'name': 'Expenses', 'url': '/expenses/'},
        {'name': 'Sales', 'url': '/sales/'},
        {'name': 'Reports', 'url': '/reports/'},
    ]
    return render(request, 'main/home.html', {'modules': modules})

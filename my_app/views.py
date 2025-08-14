from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

def employee_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'my_app/employee_form.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'my_app/employee_list.html', {'employees': employees})
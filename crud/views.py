from django.shortcuts import render, redirect
from .models import Employee,EmployeeDetail
from .forms1 import EmployeeForm
from .forms2 import EmployeeDetailForm

# Create your views here.
def index(request):
    employee = Employee.objects.all()
    employee_detail = EmployeeDetail.objects.all()
    context = {
        'employee':employee,
        'employee_detail':employee_detail
    }
    return render(request, 'crud/index.html', context)

def detail(request, id):
    employee = Employee.objects.get(pk=id)
    employee_detail = EmployeeDetail.objects.get(pk=id)
    context = {
        'employee':employee,
        'employee_detail':employee_detail
    }
    return render(request, 'crud/detail.html', context)

def add_employee(request):
    form = EmployeeForm(request.POST or None)


    if form.is_valid():
        form.save()

    return render(request,'crud/employee_form.html', {'form':form})

def add_employee_details(request):
    form = EmployeeDetailForm(request.POST or None)


    if form.is_valid():
        form.save()
        return redirect('crud:index')

    return render(request,'crud/employee_detail_form.html', {'form':form})


def update_employee(request,id):
    item = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('crud:index')
    return render(request,'crud/employee_form.html',{'form':form,'item':item})

def delete_employee(request,id):
    item = Employee.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request,'crud/item-delete.html',{'item':item})
from django.shortcuts import render,redirect
from MyApps1.models import Employee
from MyApps1.forms import EmployeeForm
# Create your views here.

def show(request):
    employees=Employee.objects.all()
    return render(request,'MyApps1/index.html',{'employees':employees})

def insert(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index')

    return render(request,'MyApps1/insert.html',{'form':form})

def delete(request,pk):
    employee=Employee.objects.get(id=pk)
    employee.delete()
    return redirect('/index')

def update(request,pk):
    employee=Employee.objects.get(id=pk)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/index')
    return render(request,'MyApps1/update.html',{'employee':employee})
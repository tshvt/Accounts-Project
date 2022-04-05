from django.shortcuts import render, redirect
from .forms import EmployeeForm, DepartmentForm, EditDepartmentForm
from .models import Employee, Department
from .functions import find_number


def index(request):
    return render(request, 'employees/index.html')


def all_employees(request):
    employees = Employee.objects.all()
    return render(
        request,
        'employees/all-employees.html',
        {'employees': employees}
    )


def all_departments(request):
    departments = Department.objects.all()
    return render(
        request,
        'employees/all-departments.html',
        {'departments': departments}
    )


def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            new_emp = Employee.objects.get(email=form.cleaned_data['email'])
            if not new_emp.rights_num:
                new_emp.rights_num = new_emp.department.rights_num
                new_emp.save()
            return redirect("all-emp")
    else:
        form = EmployeeForm()
    return render(
        request,
        "employees/new-employee.html",
        {"form": form}
    )


def create_department(request, parent_id):
    parent = Department.objects.get(pk=parent_id)
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            new_dept = Department.objects.get(name=form.cleaned_data['name'])
            new_dept.parent_department = parent
            new_dept.save()
            return redirect("all-dept")
    else:
        rights_num = find_number(parent)
        form = DepartmentForm(initial={'rights_num': rights_num})
    return render(
        request,
        "employees/new-department.html",
        {"form": form}
    )


def edit_employee(request, id):
    emp_to_update = Employee.objects.get(pk=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=emp_to_update)
        if form.is_valid():
            form.save()
            return redirect("all-emp")
    form = EmployeeForm(instance=emp_to_update)
    return render(
        request,
        "employees/new-employee.html",
        {"form": form}
    )


def edit_department(request, id):
    dept_to_update = Department.objects.get(pk=id)
    if request.method == "POST":
        form = EditDepartmentForm(request.POST, instance=dept_to_update)
        if form.is_valid():
            form.save()
            return redirect("all-dept")
    form = EditDepartmentForm(instance=dept_to_update)
    return render(
        request,
        "employees/new-department.html",
        {"form": form}
    )

from django import forms
from .models import Employee, Department


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'middle_name': 'Отчество',
            'position': 'Должность',
            'city': 'Город',
            'email': 'Электронная почта',
            'phone_number': 'Телефонный номер',
            'timezone': 'Часовой пояс',
            'department': 'Отдел',
            'rights_num': 'Число, задающее права'
        }


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'rights_num']
        labels = {
            'name': 'Название',
            'rights_num': 'Число, задающее права',
        }


class EditDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        labels = {
            'name': 'Название',
            'rights_num': 'Число, задающее права',
            'parent_department': 'Родительский отдел'
        }

import pytest
from employees.models import Department, Employee


@pytest.mark.django_db
@pytest.fixture
def department_obj():
    dept = Department.objects.create(name="Core", rights_num=1)
    dept.save()
    return dept


@pytest.mark.django_db
@pytest.fixture
def employee_obj():
    dept = Department.objects.create(name="Test", rights_num=1)
    dept.save()
    employee = Employee.objects.create(
        first_name='Имя',
        last_name='Фамилия',
        middle_name='Отчество',
        position='Должность',
        city='Город',
        email='testing@mail.com',
        phone_number='Телефонный номер',
        timezone='Часовой пояс',
        department=dept,
        rights_num=1)
    return employee


@pytest.mark.django_db
@pytest.fixture
def employee_form_data_false():
    dept = Department.objects.create(name="Test", rights_num=1)
    dept.save()
    pk = Department.objects.get(pk=dept.id).id
    form_data = {'first_name': 'Имя',
                 'last_name': 'Фамилия',
                 'middle_name': 'Отчество',
                 'position': 'Должность',
                 'city': 'Город',
                 'email': 'testttt',
                 'phone_number': 'Телефонный номер',
                 'timezone': 'Часовой пояс',
                 'department': pk,
                 'rights_num': 1}
    return form_data


@pytest.mark.django_db
@pytest.fixture
def employee_form_data_true():
    dept = Department.objects.create(name="Test", rights_num=1)
    dept.save()
    pk = Department.objects.get(pk=dept.id).id
    form_data = {'first_name': 'Имя',
                 'last_name': 'Фамилия',
                 'middle_name': 'Отчество',
                 'position': 'Должность',
                 'city': 'Город',
                 'email': 'test@mail.com',
                 'phone_number': 'Телефонный номер',
                 'timezone': 'Часовой пояс',
                 'department': pk,
                 'rights_num': 1}
    return form_data

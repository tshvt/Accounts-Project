from employees.forms import EmployeeForm, DepartmentForm

import pytest


@pytest.mark.django_db
class TestForm:

    def test_emp_form_success(self, employee_form_data_true):
        form = EmployeeForm(data=employee_form_data_true)
        assert form.is_valid()

    def test_emp_form_fail(self, employee_form_data_false):
        form = EmployeeForm(data=employee_form_data_false)
        assert not form.is_valid()

    def test_dept_form_success(self, department_obj):
        form_data = {'name': 'Отдел',
                     'parent_department': department_obj.id,
                     'rights_num': 1}
        form = DepartmentForm(data=form_data)
        assert form.is_valid()

    def test_dept_form_fail(self, department_obj):
        form_data = {'parent_department': department_obj.id,
                     'rights_num': 1}
        form = DepartmentForm(data=form_data)
        assert not form.is_valid()

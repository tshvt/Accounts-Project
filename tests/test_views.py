from django.urls import reverse
import pytest
from employees.models import Department, Employee


@pytest.mark.django_db
class TestViews:

    @pytest.mark.parametrize('param', [
        ('index'),
        ('new-emp'),
        ('all-emp'),
        ('all-dept'),
    ])
    def test_render_views(self, client, param):
        temp_url = reverse(param)
        response = client.get(temp_url)
        assert response.status_code == 200

    def test_render_views_new_dept(self, client, department_obj):
        temp_url = reverse('new-dept', kwargs={'parent_id': 1})
        response = client.get(temp_url)
        assert response.status_code == 200

    def test_render_views_edit_dept(self, client, department_obj):
        temp_url = reverse('edit-dept', kwargs={'id': 1})
        response = client.get(temp_url)
        assert response.status_code == 200

    def test_render_views_edit_emp(self, client, employee_obj):
        temp_url = reverse('edit-emp', kwargs={'id': employee_obj.id})
        response = client.get(temp_url)
        assert response.status_code == 200

    def test_create_emp(self, client, employee_form_data_true):
        assert Employee.objects.count() == 0
        new_emp_url = reverse('new-emp')
        response = client.post(new_emp_url, employee_form_data_true)
        assert Employee.objects.count() == 1
        assert response.status_code == 302

    def test_create_dept(self, client, department_obj):
        assert Department.objects.count() == 1
        new_dept_url = reverse('new-dept', kwargs={'parent_id': 1})
        form_data = {'name': 'Отдел',
                     'parent_department': department_obj.id,
                     'rights_num': 1}
        response = client.post(new_dept_url, form_data)
        assert Department.objects.count() == 2
        assert response.status_code == 302

    def test_edit_emp(self, client, employee_obj):
        edit_emp_url = reverse('edit-emp', kwargs={'id': employee_obj.id})
        assert employee_obj.email == "testing@mail.com"
        response = client.get(edit_emp_url)
        form = response.context['form']
        data = form.initial
        data['email'] = 'test@mail.com'
        response = client.post(edit_emp_url, data)
        assert response.status_code == 302
        response = client.get(edit_emp_url)
        assert response.context['form'].initial['email'] == 'test@mail.com'

    def test_edit_dept(self, client, department_obj):
        new_dept = Department.objects.create(name="Test", rights_num=1, parent_department=department_obj)
        new_dept.save()
        assert new_dept.name == 'Test'
        edit_dept_url = reverse('edit-dept', kwargs={'id': new_dept.id})
        response = client.get(edit_dept_url)
        form = response.context['form']
        data = form.initial
        data['name'] = 'NewName'
        response = client.post(edit_dept_url, data)
        assert response.status_code == 302
        response = client.get(edit_dept_url)
        assert response.context['form'].initial['name'] == 'NewName'

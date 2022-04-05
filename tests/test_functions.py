from employees.functions import find_number
from employees.models import Department
import pytest


@pytest.mark.django_db
class TestFunctions:

    def test_function_success(self):
        core = Department.objects.create(name="Core", rights_num=1)
        core.save()
        parent = Department.objects.create(name="Parent", parent_department=core)
        parent.save()
        number = find_number(parent)
        assert number == 1

import pytest
from mixer.backend.django import mixer
from django.core.exceptions import ValidationError


@pytest.mark.django_db
class TestModels:

    def test_rights_num_validators_min(self):
        employee = mixer.blend('employees.Employee', rights_num=-1)
        department = mixer.blend('employees.Department', rights_num=-1)
        with pytest.raises(ValidationError):
            employee.full_clean()
            department.full_clean()

    def test_rights_num_validators_max(self):
        employee = mixer.blend('employees.Employee', rights_num=1024)
        department = mixer.blend('employees.Department', rights_num=1024)
        with pytest.raises(ValidationError):
            employee.full_clean()
            department.full_clean()

    def test_rights_num_validators(self):
        employee = mixer.blend('employees.Employee', rights_num=10)
        department = mixer.blend('employees.Department', rights_num=10)
        employee.full_clean()
        department.full_clean()
        assert employee.rights_num == 10
        assert department.rights_num == 10

    def test_email_validator_not_validates(self):
        employee = mixer.blend('employees.Employee', email='kdkskjfs')
        with pytest.raises(ValidationError):
            employee.full_clean()

    def test_email_validator_validates(self):
        employee = mixer.blend('employees.Employee', email='kdkskjfs@mail.com')
        employee.full_clean()
        assert employee.email == 'kdkskjfs@mail.com'

from django.urls import reverse, resolve


class TestUrls:

    def test_index_url(self):
        path = reverse('index')
        assert resolve(path).view_name == 'index'

    def test_new_emp_url(self):
        path = reverse('new-emp')
        assert resolve(path).view_name == 'new-emp'

    def test_new_dept_url(self):
        path = reverse('new-dept', kwargs={'parent_id': 1})
        assert resolve(path).view_name == 'new-dept'

    def test_all_emp_url(self):
        path = reverse('all-emp')
        assert resolve(path).view_name == 'all-emp'

    def test_all_dept_url(self):
        path = reverse('all-dept')
        assert resolve(path).view_name == 'all-dept'

    def test_edit_emp_url(self):
        path = reverse('edit-emp', kwargs={'id': 1})
        assert resolve(path).view_name == 'edit-emp'

    def test_edit_dept_url(self):
        path = reverse('edit-dept', kwargs={'id': 1})
        assert resolve(path).view_name == 'edit-dept'

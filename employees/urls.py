from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new-employee", views.create_employee, name="new-emp"),
    path("new-department/<int:parent_id>", views.create_department, name="new-dept"),
    path("all-employees", views.all_employees, name="all-emp"),
    path("all-departments", views.all_departments, name="all-dept"),
    path("edit-employee/<int:id>", views.edit_employee, name="edit-emp"),
    path("edit-department/<int:id>", views.edit_department, name="edit-dept")

]

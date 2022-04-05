from .models import Department


def find_number(parent):
    """
    Функция для поиска числа, задающего права, у родителей и прародителей отдела.
    """
    if parent.rights_num is None:
        while parent.rights_num is None:
            parent = Department.objects.get(name=parent.parent_department)
        return parent.rights_num
    else:
        return parent.rights_num

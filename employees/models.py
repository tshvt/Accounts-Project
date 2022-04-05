from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    rights_num = models.IntegerField(
        validators=[MaxValueValidator(1023),
                    MinValueValidator(0)],
        blank=True,
        null=True
    )
    parent_department = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        to_field='name',
        null=True,
    )

    def __str__(self):
        return "{}".format(self.name)


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    position = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    timezone = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    rights_num = models.IntegerField(
        validators=[MaxValueValidator(1023),
                    MinValueValidator(0)],
        blank=True,
        null=True
    )

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

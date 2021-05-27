from django.db import models

# Create your models here.
from employee.models import Employee


class Attandance(models.Model):

    status_choices = (
        ("Present", "Present"),
        ("Leave", "Leave"),
        ("Absent", "Absent")

    )

    status = models.CharField(max_length=100,choices=status_choices,default='Present')
    # emp_attandande = models.CharField(max_length=100, default=None)
    emp_attandande = models.ForeignKey(Employee, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(auto_now_add=True)
    # emp_date = models.DateField()


    def __str__(self):
        return self.status
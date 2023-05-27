from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Employes(models.Model):
    name =models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100)
    age = models.IntegerField()
    date_of_joining = models.DateField()

# class Department(models.Model):
#     DepartmentId = models.CharField(max_length=100)
#     DepartmentName = models.CharField(max_length=100)
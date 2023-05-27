from rest_framework import serializers
from .models import Employes

# class DepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Department
#         fields=('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employes
        fields= '__all__'
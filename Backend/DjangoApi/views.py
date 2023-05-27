from rest_framework.response import Response
from .models import Employes
from .serilizers import EmployeeSerializer
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend


@api_view(['GET'])
def getEmpList(request):
    Emp = Employes.objects.all()
    serializer = EmployeeSerializer(Emp, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEmpDetail(request, pk):
    Emp = Employes.objects.get(id=pk)
    serializer = EmployeeSerializer(Emp, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createEmp(request):
    serializer = EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateEmp(request, pk):
    product = Employes.objects.get(id=pk)
    serializer = EmployeeSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def filterEmp(request, name):
    emp = Employes.objects.filter(name=name)
    serializer = EmployeeSerializer(emp, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def deleteEmp(request, pk):
    emp = Employes.objects.get(id=pk)
    emp.delete()

    return Response('Items delete successfully!')



from django.urls import path
from . import views


urlpatterns = [
    path('', views.getEmpList, name="emp-list"),
    path('create/', views.createEmp, name="create-emp"),
    path('<str:pk>/update/', views.updateEmp, name="update-emp"),
    path('<str:pk>/delete/', views.deleteEmp, name="delete-emp"),
    path('<str:name>/', views.filterEmp, name='filter-employees'),
    path('<str:pk>/', views.getEmpDetail, name="Emp"),
]


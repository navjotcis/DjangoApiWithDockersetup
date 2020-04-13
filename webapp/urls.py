from django.urls import path

from . import views

urlpatterns = [
    path('employees/', views.EmployeeList.as_view()),
    path('employees/<int:id>', views.EmployeeDetailView.as_view()),
]

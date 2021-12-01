from django.urls import path
from firstApp import views


urlpatterns = [
    path('emps/',views.employeeView),
    path('students/',views.student_list),
    path('students/<int:pk>/',views.student_detail),
]

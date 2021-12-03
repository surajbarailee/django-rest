from django.urls import path,include
from firstApp import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('students', views.StudentViewSet)


# urlpatterns = [
#     path('emps/',views.employeeView),
#     path('students/',views.StudentList.as_view()),
#     path('students/<int:pk>/',views.StudentDetail.as_view()),
# ]


urlpatterns = [
    path('',include(router.urls)),
]
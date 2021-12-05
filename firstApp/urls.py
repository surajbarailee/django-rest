from django.urls import path,include
from firstApp import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('students', views.StudentViewSet)
router.register('books', views.BookViewSet)
router.register('author', views.AuthorViewSet)


# urlpatterns = [
#     path('emps/',views.employeeView),
#     path('students/',views.StudentList.as_view()),
#     path('students/<int:pk>/',views.StudentDetail.as_view()),
# ]


urlpatterns = [
    path('',include(router.urls)),
    path('api-token-auth/',obtain_auth_token,name='api_token_auth')
]
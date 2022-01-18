from django.urls import path
from . import viewsets

app_name = 'accounts'
urlpatterns = [
    path('users/', viewsets.UserList.as_view()),
    path('users/<int:pk>/', viewsets.UserDetail.as_view()),
]

from django.urls import path
from . import viewsets

urlpatterns = [
    path('carbrands/', viewsets.CarBrandList.as_view()),
    path('carbrands/<int:pk>/', viewsets.CarBrandDetail.as_view()),
    path('carmodels/', viewsets.CarModelList.as_view()),
    path('carmodels/<int:pk>/', viewsets.CarModelDetail.as_view()),
    path('usercars/', viewsets.UserCarList.as_view()),
    path('usercars/<int:pk>/', viewsets.UserCarDetail.as_view()),
]

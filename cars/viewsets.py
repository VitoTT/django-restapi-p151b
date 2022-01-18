from cars.models import CarBrand, CarModel, UserCar
from cars.serializers import CarBrandSerializer, CarModelSerializer, UserCarSerializer
from rest_framework import generics
import django_filters.rest_framework


class CarBrandList(generics.ListCreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name']


class CarBrandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarModelList(generics.ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'car_brand']


class CarModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class UserCarList(generics.ListCreateAPIView):
    queryset = UserCar.objects.all()
    serializer_class = UserCarSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['user', 'car_brand', 'car_model', 'first_reg', 'odo']


class UserCarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserCar.objects.all()
    serializer_class = UserCarSerializer

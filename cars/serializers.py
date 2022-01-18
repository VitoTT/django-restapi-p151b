from cars.models import CarBrand, CarModel, UserCar
from rest_framework import serializers


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ['id', 'name']


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'name', 'car_brand']


class UserCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCar
        fields = ['id', 'user', 'car_brand', 'car_model', 'first_reg', 'odo']

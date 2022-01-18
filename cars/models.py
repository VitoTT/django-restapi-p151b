from django.db import models
from accounts.models import User
from .softdelete import SoftDeleteModel


class CarBrand(SoftDeleteModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CarModel(SoftDeleteModel):
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class UserCar(SoftDeleteModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    first_reg = models.DateTimeField('first registration')
    odo = models.PositiveIntegerField('odometer')

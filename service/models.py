from django.contrib.auth.models import AbstractUser
from django.db import models

from restaurant_kitchen_service import settings


class DishType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    password = models.CharField(max_length=100)
    years_of_experience = models.IntegerField(default=0)

    class Meta:
        ordering = ("username", )


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name", )


class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dishes")
    ingredients = models.ManyToManyField(Ingredient, related_name="dishes")

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return f"{self.name} (price: {self.price}, dish type: {self.dish_type})"

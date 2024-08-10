from django.contrib.auth.models import AbstractUser
from django.db import models

from restaurant_kitchen_service import settings


class DishType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("id", )

    def __str__(self) -> str:
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    class Meta:
        ordering = ("id", )

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)

    class Meta:
        ordering = ("id", )

    def __str__(self) -> str:
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="dishes"
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name="dishes",
        blank=True)

    class Meta:
        ordering = ("dish_type", "name", )
        verbose_name_plural = "Dishes"

    def __str__(self) -> str:
        return f"{self.name} (price: {self.price}, dish type: {self.dish_type})"

from django.contrib.auth import get_user_model
from django.test import TestCase

from service.models import DishType, Cook, Ingredient, Dish


class ModelsTests(TestCase):

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="Dish Type")
        self.assertEqual(str(dish_type), "Dish Type")

    def test_cook_str(self):
        cook = Cook.objects.create(
            username="Cook",
            first_name="Test1",
            last_name="Test2"
        )
        self.assertEqual(str(cook), "Cook (Test1 Test2)")

    def test_ingredient_str(self):
        ingredient = Ingredient.objects.create(name="Test")
        self.assertEqual(str(ingredient), "Test")

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="Dish Type")
        dish = Dish.objects.create(name="Test", dish_type=dish_type, price=100)
        self.assertEqual(str(dish), "Test (price: 100, dish type: Dish Type)")

    def test_create_cook_with_years_of_experience(self):
        username = "Test"
        password = "<PASSWORD>"
        years_of_experience = 20
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience
        )
        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.years_of_experience, years_of_experience)

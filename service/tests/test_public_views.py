from django.test import TestCase

from django.urls import reverse

from service.models import (
    DishType,
    Cook,
    Dish,
    Ingredient
)

DISH_TYPE_VIEW_LIST_URL = reverse("service:dish-type-list")
DISH_TYPE_CREATE_VIEW_URL = reverse("service:dish-type-create")

DISH_VIEW_LIST_URL = reverse("service:dish-list")
DISH_CREATE_VIEW_URL = reverse("service:dish-create")

COOK_VIEW_LIST_URL = reverse("service:cook-list")
COOK_CREATE_VIEW_URL = reverse("service:cook-create")

INGREDIENT_VIEW_LIST_URL = reverse("service:ingredient-list")
INGREDIENT_CREATE_VIEW_URL = reverse("service:ingredient-create")


class PublicViewsTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Dish Test")
        self.cook = Cook.objects.create(
            username="Cook Test",
            password="<PASSWORD>",
        )
        self.dish = Dish.objects.create(
            name="Dish Test",
            dish_type=self.dish_type,
            price=10
        )
        self.ingredient = Ingredient.objects.create(name="Ingredient Test")

    def test_dish_type_list_view(self):
        response = self.client.get(DISH_TYPE_VIEW_LIST_URL)
        self.assertNotEquals(response.status_code, 200)

    def test_dish_type_create_view(self):
        response = self.client.get(DISH_TYPE_CREATE_VIEW_URL)
        self.assertNotEquals(response.status_code, 200)

    def test_dish_type_update_view(self):
        dish_type_update_view_url = reverse(
            "service:dish-type-update",
            args=[self.dish_type.id]
        )
        response = self.client.get(dish_type_update_view_url)
        self.assertNotEquals(response.status_code, 200)

    def test_dish_type_delete_view(self):
        dish_type_delete_view_url = reverse(
            "service:dish-type-delete",
            args=[self.dish_type.id]
        )
        response = self.client.get(dish_type_delete_view_url)
        self.assertNotEquals(response.status_code, 200)

    def test_cook_list_view(self):
        response = self.client.get(COOK_VIEW_LIST_URL)
        self.assertNotEquals(response.status_code, 200)

    def test_cook_detail_view(self):
        cook_detail_view_url = reverse(
            "service:cook-detail",
            args=[self.cook.id]
        )
        response = self.client.get(cook_detail_view_url)
        self.assertNotEquals(response.status_code, 200)

    def test_cook_create_view(self):
        response = self.client.get(COOK_CREATE_VIEW_URL)
        self.assertNotEquals(response.status_code, 200)

    def test_cook_years_of_experience_update_view(self):
        cook_years_of_experience_update_view_url = reverse(
            "service:cook-years-of-experience-update",
            args=[self.cook.id]
        )
        response = self.client.get(cook_years_of_experience_update_view_url)
        self.assertNotEquals(response.status_code, 200)

    def test_cook_delete_view(self):
        cook_delete_view_url = reverse(
            "service:cook-delete",
            args=[self.cook.id]
        )
        response = self.client.get(cook_delete_view_url)
        self.assertNotEquals(response.status_code, 200)

    def test_dish_list_view(self):
        response = self.client.get(DISH_VIEW_LIST_URL)
        self.assertNotEquals(response.status_code, 200)

    def test_dish_detail_view(self):
        dish_detail_view_url = reverse(
            "service:dish-detail",
            args=[self.dish.id]
        )
        response = self.client.get(dish_detail_view_url)
        self.assertNotEquals(response.status_code, 200)

    def test_dish_create_view(self):
        response = self.client.get(DISH_CREATE_VIEW_URL)
        self.assertNotEquals(response.status_code, 200)

    def test_dish_update_view(self):
        dish_update_view_url = reverse(
            "service:dish-update",
            args=[self.dish.id]
        )
        response = self.client.get(dish_update_view_url)
        self.assertNotEquals(response.status_code, 200)

    def test_dish_delete_view(self):
        dish_delete_view_url = reverse(
            "service:dish-delete",
            args=[self.dish.id]
        )
        response = self.client.get(dish_delete_view_url)
        self.assertNotEquals(response.status_code, 200)

    def test_ingredient_list_view(self):
        response = self.client.get(INGREDIENT_VIEW_LIST_URL)
        self.assertNotEquals(response.status_code, 200)

    def test_ingredient_create_view(self):
        response = self.client.get(INGREDIENT_CREATE_VIEW_URL)
        self.assertNotEquals(response.status_code, 200)

    def test_ingredient_update_view(self):
        ingredient_update_view_url = reverse(
            "service:ingredient-update",
            args=[self.ingredient.id]
        )
        response = self.client.get(ingredient_update_view_url)
        self.assertNotEqual(response.status_code, 200)

    def test_ingredient_delete_view(self):
        ingredient_delete_view_url = reverse(
            "service:ingredient-delete",
            args=[self.ingredient.id]
        )
        response = self.client.get(ingredient_delete_view_url)
        self.assertNotEquals(response.status_code, 200)

from django.contrib.auth import get_user_model
from django.test import TestCase

from django.urls import reverse

from service.models import DishType, Dish, Ingredient, Cook

DISH_TYPE_VIEW_LIST_URL = reverse("service:dish-type-list")
DISH_TYPE_CREATE_VIEW_URL = reverse("service:dish-type-create")

DISH_VIEW_LIST_URL = reverse("service:dish-list")
DISH_CREATE_VIEW_URL = reverse("service:dish-create")

COOK_VIEW_LIST_URL = reverse("service:cook-list")
COOK_CREATE_VIEW_URL = reverse("service:cook-create")

INGREDIENT_VIEW_LIST_URL = reverse("service:ingredient-list")
INGREDIENT_CREATE_VIEW_URL = reverse("service:ingredient-create")


class ViewsPrivateTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpass"
        )
        self.client.force_login(self.user)

    def test_dish_type_list_view(self):
        DishType.objects.create(name="Desserts")
        DishType.objects.create(name="Pizza")
        response = self.client.get(DISH_TYPE_VIEW_LIST_URL)
        self.assertEqual(response.status_code, 200)
        list_dish_types = DishType.objects.all()
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(list_dish_types))
        self.assertTemplateUsed(response, "service/dish_type_list.html")

    def test_dish_type_create_view(self):
        dish_type = DishType.objects.create(name="desserts")
        response = self.client.get(DISH_TYPE_CREATE_VIEW_URL)
        self.assertEqual(response.status_code, 200)
        res = self.client.get(DISH_TYPE_VIEW_LIST_URL)
        self.assertContains(res, dish_type.name)
        self.assertTemplateUsed(response, "service/dish_type_form.html")

    def test_dish_type_update_view(self):
        dish_type = DishType.objects.create(name="desserts")
        dish_type_update_url_view = reverse(
            "service:dish-type-update",
            kwargs={"pk": dish_type.id})
        response = self.client.get(dish_type_update_url_view)
        self.assertEqual(response.status_code, 200)
        new_dish_type = DishType.objects.get(id=dish_type.id)
        new_dish_type.name = "pizza"
        new_dish_type.save()
        res = self.client.get(DISH_TYPE_VIEW_LIST_URL)
        self.assertContains(res, new_dish_type.name)
        self.assertTemplateUsed(response, "service/dish_type_form.html")

    def test_dish_type_delete_view(self):
        dish_type = DishType.objects.create(name="desserts")
        dish_type_delete_url_view = reverse(
            "service:dish-type-delete",
            kwargs={"pk": dish_type.id})
        response = self.client.get(dish_type_delete_url_view)
        self.assertEqual(response.status_code, 200)
        DishType.objects.get(id=dish_type.id).delete()
        res = self.client.get(DISH_TYPE_VIEW_LIST_URL)
        self.assertNotContains(res, dish_type)
        self.assertTemplateUsed("service/dish_type_confirm_delete.html")

    def test_retrieve_dish_list_view(self):
        dish_type = DishType.objects.create(name="desserts")
        Dish.objects.create(name="ice cream", dish_type=dish_type, price=10)
        response = self.client.get(DISH_VIEW_LIST_URL)
        self.assertEqual(response.status_code, 200)
        list_dishes = Dish.objects.all()
        self.assertEqual(list(response.context["dish_list"]), list(list_dishes))
        self.assertTemplateUsed(response, "service/dish_list.html")

    def test_create_dish_view(self):
        dish_type = DishType.objects.create(name="desserts")
        dish = Dish.objects.create(name="ice cream", dish_type=dish_type, price=10)
        response = self.client.get(DISH_CREATE_VIEW_URL)
        self.assertEqual(response.status_code, 200)
        res = self.client.get(DISH_VIEW_LIST_URL)
        self.assertContains(res, dish.name)
        self.assertContains(res, dish_type.name)
        self.assertContains(res, dish.price)
        self.assertTemplateUsed(response, "service/dish_form.html")

    def test_update_dish_view(self):
        dish_type = DishType.objects.create(name="desserts")
        dish_type_second = DishType.objects.create(name="pizza")
        dish = Dish.objects.create(name="Carbonara", dish_type=dish_type, price=10)
        dish_update_url_view = reverse(
            "service:dish-update",
            kwargs={"pk": dish.id}
        )
        response = self.client.get(dish_update_url_view)
        self.assertEqual(response.status_code, 200)
        new_dish = Dish.objects.get(id=dish.id)
        new_dish.name = "Margarita"
        new_dish.dish_type = dish_type_second
        new_dish.save()
        res = self.client.get(DISH_VIEW_LIST_URL)
        self.assertContains(res, new_dish.name)
        self.assertContains(res, dish_type_second.name)
        self.assertTemplateUsed(response, "service/dish_form.html")

    def test_dish_delete_view(self):
        dish_type = DishType.objects.create(name="pizza")
        dish = Dish.objects.create(name="Carbonara", dish_type=dish_type, price=10)
        dish_delete_url_view = reverse(
            "service:dish-delete",
            kwargs={"pk": dish.id}
        )
        response = self.client.get(dish_delete_url_view)
        self.assertEqual(response.status_code, 200)
        dish.delete()
        res = self.client.get(DISH_VIEW_LIST_URL)
        self.assertNotContains(res, dish)
        self.assertTemplateUsed(response, "service/dish_confirm_delete.html")

    def test_dish_detail_view(self):
        cook = Cook.objects.create(
            username="Dimakop",
            password="<PASSWORD>",
            first_name="Dima",
            last_name="Dobkin"
        )
        dish_type = DishType.objects.create(name="pizza")
        ingredient = Ingredient.objects.create(name="flour")
        dish = Dish.objects.create(
            name="Carbonara",
            dish_type=dish_type,
            price=10,
        )
        dish.cooks.add(cook)
        dish.ingredients.add(ingredient)
        dish.save()
        dish_detail_url_view = reverse(
            "service:dish-detail",
            kwargs={"pk": dish.id}
        )
        response = self.client.get(dish_detail_url_view)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, ingredient.name)
        self.assertContains(response, cook.first_name)
        self.assertContains(response, cook.last_name)
        self.assertTemplateUsed(response, "service/dish_detail.html")



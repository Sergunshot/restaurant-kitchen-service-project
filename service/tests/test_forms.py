from django.test import TestCase

from service.forms import (
    DishSearchForm,
    CookSearchForm,
    IngredientSearchForm,
    CookCreationForm
)


class FormsTest(TestCase):
    def test_cook_creation_form_with_is_valid(self):
        form_data = {
            "username": "valuc",
            "password1": "Test22021994",
            "password2": "Test22021994",
            "email": "Email@email.com",
            "first_name": "Dmitriy",
            "last_name": "Dobkin",
            "years_of_experience": 5
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_dish_search_form(self):
        form_data = {
            "name": "Test"
        }
        form = DishSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_ingredient_search_form(self):
        form_data = {
            "name": "Test"
        }
        form = IngredientSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_cook_search_form(self):
        form_data = {
            "username": "Test",
        }
        form = CookSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

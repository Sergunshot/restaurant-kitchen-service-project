from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from service.models import Cook


class AdminSiteTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="passtest"
        )
        self.client.force_login(self.admin_user)
        self.cook = Cook.objects.create(
            username="adminname",
            password="<PASSWORD>",
            years_of_experience=3
        )

    def test_driver_license_number_listed(self):
        """
        Test that years of experience listed on cook admin page
        """
        url = reverse("admin:service_cook_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)

    def test_driver_detail_license_number_listed_(self):
        """
        Test that years of experience listed on cook detail admin page
        """
        url = reverse("admin:service_cook_change", args=[self.cook.id])
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)

    def test_driver_info_listed_(self):
        """
        Test that years of experience, first name, last
        name listed on cook detail add admin page
        """
        url = reverse("admin:service_cook_add")
        res = self.client.get(url)
        self.assertContains(res, "years_of_experience")
        self.assertContains(res, "first_name")
        self.assertContains(res, "last_name")

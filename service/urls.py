from django.urls import path

from service.views import index, DishTypesListView

urlpatterns = [
    path("", index, name="index"),
    path("dish_types/", DishTypesListView.as_view(), name="dish-types-list"),
]

app_name = "service"

from django.urls import path

from service.views import index, DishTypesListView, DishListView

urlpatterns = [
    path("", index, name="index"),
    path("dish_types/", DishTypesListView.as_view(), name="dish-types-list"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
]

app_name = "service"

from django.urls import path

from service.views import index, DishTypesListView, DishListView, DishDetailView

urlpatterns = [
    path("", index, name="index"),
    path("dish_types/", DishTypesListView.as_view(), name="dish-types-list"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>", DishDetailView.as_view(), name="dish-detail"),
]

app_name = "service"

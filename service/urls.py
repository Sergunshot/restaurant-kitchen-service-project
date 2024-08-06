from django.urls import path

from service.views import index, DishTypesListView, DishListView, DishDetailView, CooksListView, \
    CookDetailView

urlpatterns = [
    path("", index, name="index"),
    path("dish_types/", DishTypesListView.as_view(), name="dish-types-list"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>", DishDetailView.as_view(), name="dish-detail"),
    path("cooks/", CooksListView.as_view(), name="cooks-list"),
    path("cooks/<int:pk>", CookDetailView.as_view(), name="cooks-detail"),
]

app_name = "service"

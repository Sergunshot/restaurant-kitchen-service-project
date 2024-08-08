from django.urls import path

from service.views import index, DishTypesListView, DishListView, DishDetailView, CooksListView, \
    CookDetailView, DishTypeCreateView, DishTypeUpdateView, DishTypeDeleteView, DishCreateView, DishUpdateView, \
    DishDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("dish_types/", DishTypesListView.as_view(), name="dish-types-list"),
    path("dish_type/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish_type/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish_type/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("cooks/", CooksListView.as_view(), name="cooks-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cooks-detail"),
]

app_name = "service"

from django.urls import path

from service.views import index, DishListView, DishDetailView, \
    CookDetailView, DishTypeCreateView, DishTypeUpdateView, DishTypeDeleteView, DishCreateView, DishUpdateView, \
    DishDeleteView, DishTypeListView, CookListView, IngredientListView, IngredientCreateView, IngredientUpdateView, \
    IngredientDeleteView, CookCreateView

urlpatterns = [
    path("", index, name="index"),
    path("dish_types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish_type/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish_type/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish_type/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cooks-detail"),
    path("cook/create/", CookCreateView.as_view(), name="cook-create"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("ingredient/create/", IngredientCreateView.as_view(), name="ingredient-create"),
    path("ingredient/<int:pk>/update/", IngredientUpdateView.as_view(), name="ingredient-update"),
    path("ingredient/<int:pk>/delete/", IngredientDeleteView.as_view(), name="ingredient-delete"),
]

app_name = "service"

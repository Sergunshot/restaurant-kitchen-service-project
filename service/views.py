from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from service.forms import (
    DishForm,
    DishSearchForm,
    IngredientSearchForm,
    CookSearchForm,
    CookYearsOfExperienceUpdateForm,
    CookCreationForm
)
from service.models import Cook, DishType, Dish, Ingredient


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_cooks = Cook.objects.count()
    num_dish_types = DishType.objects.count()
    num_dishes = Dish.objects.count()
    num_ingredients = Ingredient.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        "num_cooks": num_cooks,
        "num_dish_types": num_dish_types,
        "num_dishes": num_dishes,
        "num_visits": num_visits,
        "num_ingredients": num_ingredients,
    }
    return render(request, "service/index.html", context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    paginate_by = 7
    template_name = "service/dish_type_list.html"
    queryset = DishType.objects.all()
    context_object_name = "dish_type_list"


class DishTypeCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = DishType
    success_url = reverse_lazy("service:dish-type-list")
    fields = "__all__"
    template_name = "service/dish_type_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = DishType
    success_url = reverse_lazy("service:dish-type-list")
    fields = "__all__"
    template_name = "service/dish_type_form.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = DishType
    success_url = reverse_lazy("service:dish-type-list")
    template_name = "service/dish_type_confirm_delete.html"


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 7
    template_name = "service/dish_list.html"
    queryset = Dish.objects.select_related(
        "dish_type").prefetch_related("ingredients")
    context_object_name = "dish_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Dish.objects.select_related(
            "dish_type").prefetch_related("ingredients")
        form = DishSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.edit.CreateView):
    form_class = DishForm
    success_url = reverse_lazy("service:dish-list")
    template_name = "service/dish_form.html"


class DishUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    form_class = DishForm
    queryset = Dish.objects.all()
    success_url = reverse_lazy("service:dish-list")
    template_name = "service/dish_form.html"


class DishDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Dish
    success_url = reverse_lazy("service:dish-list")
    template_name = "service/dish_confirm_delete.html"


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5
    template_name = "service/cook_list.html"
    context_object_name = "cook_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = CookSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = Cook.objects.all()
        form = CookSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.prefetch_related("dishes")


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = CookCreationForm
    success_url = reverse_lazy("service:cook-list")
    template_name = "service/cook_form.html"


class CookDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Cook
    success_url = reverse_lazy("service:cook-list")
    template_name = "service/cook_confirm_delete.html"


class CookYearsOfExperienceUpdateView(
    LoginRequiredMixin,
    generic.edit.UpdateView
):
    model = Cook
    form_class = CookYearsOfExperienceUpdateForm
    success_url = reverse_lazy("service:cook-list")


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    paginate_by = 7
    template_name = "service/ingredient_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IngredientListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = IngredientSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Ingredient.objects.all()
        form = IngredientSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    success_url = reverse_lazy("service:ingredient-list")
    fields = "__all__"
    template_name = "service/ingredient_form.html"


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    success_url = reverse_lazy("service:ingredient-list")
    fields = "__all__"
    template_name = "service/ingredient_form.html"


class IngredientDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("service:ingredient-list")
    template_name = "service/ingredient_confirm_delete.html"

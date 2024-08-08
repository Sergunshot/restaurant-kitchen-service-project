from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from service.models import Cook, DishType, Dish


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_cooks = Cook.objects.count()
    num_dish_types = DishType.objects.count()
    num_dishes = Dish.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        "num_cooks": num_cooks,
        "num_dish_types": num_dish_types,
        "num_dishes": num_dishes,
        "num_visits": num_visits,
    }
    return render(request, "service/index.html", context)


class DishTypesListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    paginate_by = 5
    template_name = "service/dish_types_list.html"
    queryset = DishType.objects.all()
    context_object_name = "dish_types_list"


class DishTypeCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = DishType
    success_url = reverse_lazy("service:dish-types-list")
    fields = "__all__"
    template_name = "service/dish_type_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = DishType
    success_url = reverse_lazy("service:dish-types-list")
    fields = "__all__"
    template_name = "service/dish_type_form.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = DishType
    success_url = reverse_lazy("service:dish-types-list")
    template_name = "service/dish_type_confirm_delete.html"


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5
    template_name = "service/dish_list.html"
    queryset = Dish.objects.select_related('dish_type').prefetch_related("ingredients")
    context_object_name = "dish_list"


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Dish
    success_url = reverse_lazy("service:dish-list")
    fields = "__all__"
    template_name = "service/dish_form.html"


class CooksListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5
    template_name = "service/cooks_list.html"
    context_object_name = "cook_list"


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.prefetch_related("dishes")



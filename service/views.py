from django.http import HttpRequest, HttpResponse

from django.shortcuts import render
from django.views import generic

from service.models import Cook, DishType, Dish


def index(request: HttpRequest) -> HttpResponse:
    num_cooks = Cook.objects.count()
    num_dish_types = DishType.objects.count()
    num_dishes = Dish.objects.count()
    context = {
        'num_cooks': num_cooks,
        'num_dish_types': num_dish_types,
        'num_dishes': num_dishes
    }
    return render(request, 'service/index.html', context)


class DishTypesListView(generic.ListView):
    model = DishType
    paginate_by = 5
    template_name = 'service/dish_types_list.html'
    queryset = DishType.objects.all()
    context_object_name = 'dish_types_list'


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5
    template_name = 'service/dish_list.html'
    queryset = Dish.objects.select_related('dish_type').prefetch_related("ingredients")
    context_object_name = 'dish_list'


class DishDetailView(generic.DetailView):
    model = Dish


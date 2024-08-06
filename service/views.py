from django.http import HttpRequest, HttpResponse

from django.shortcuts import render

from service.models import Cook, DishType, Dish


def index(request: HttpRequest) -> HttpResponse:
    num_cooks = Cook.objects.count()
    num_dishes_type = DishType.objects.count()
    num_dishes = Dish.objects.count()
    context = {
        'num_cooks': num_cooks,
        'num_dishes_type': num_dishes_type,
        'num_dishes': num_dishes
    }
    return render(request, 'service/index.html', context)

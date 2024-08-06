from django.urls import path

from service.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "service"

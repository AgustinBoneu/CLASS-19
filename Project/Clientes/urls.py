from django.urls import path
from .views import index

app_name = "Clientes"

urlpatterns = [
    path("", index, name='index'),
]
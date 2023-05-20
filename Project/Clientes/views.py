from django.shortcuts import render
from .models import Cliente
from .models import Pais

# Create your views here.
def index(request):
    clientes = Cliente.objects.all() # Trae toda la BBDD Clientes
    datos = {"Clientes" : clientes} 
    return render(request, 'Clientes/index_Clientes.html',datos)


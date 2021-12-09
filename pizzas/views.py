from django.shortcuts import render
from .models import Pizza, Topping
# Create your views here.
def index(request):
    """Home Page"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.filter()
    context = {"pizzas":pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by()
    context = {"pizza":pizza, "toppings":toppings}
    return render(request, 'pizzas/pizza.html',context)

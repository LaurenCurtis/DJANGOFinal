from django.shortcuts import render,redirect

from pizzas.forms import CommentForm
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

def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form =CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()

            return redirect('pizzas:new_comment', pizza_id=pizza_id )
    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizzas/new_comment.html', context)

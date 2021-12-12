from django.urls import path
from . import views 
from django.conf.urls import url
from django.urls.resolvers import URLPattern
app_name = 'pizzas'

urlpatterns = [
    path('',views.index,name='index'),
    path('Pizzas',views.pizzas,name = "pizzas" ),
    path('pizzas/<int:pizza_id>/',views.pizza,name="pizza"),
    path('pizzas/<int:pizza_id>/',views.new_comment,name = 'new_comment'),
    
    
]
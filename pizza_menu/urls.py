from django.urls import path
from . import views

app_name = 'pizza_menu'

urlpatterns = [
    path('', views.menu_view, name='menu'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('order-confirmation/', views.order_confirmation_view, name='order_confirmation'),
    path('api/toppings/', views.get_toppings, name='get_toppings'),
    path('api/cart/add/', views.add_to_cart, name='add_to_cart'),
    path('about/', views.about_view, name='about'),
]

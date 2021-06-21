from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_home, name='cart_home'),
    path('api/cart/', views.cart_deatil_api_view, name='api-cart'),
    path('update/', views.cart_update, name='cart_update'),
    path('checkout/', views.checkout_home, name='checkout'),
    path('payment/', views.payment, name='payment')
] 

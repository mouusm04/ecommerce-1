from django.urls import path
from . import views

urlpatterns = [
    path('checkout/address/', views.checkout_address_create_view, name='checkout_address_create_view'),
]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_page, name='about_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register_page, name='register_page'),
    path('catagory/', views.catagory, name='catagory'),
    path('search/', views.search, name='search'),
    path('returnAndorder/', views.returnAndorder, name='returnAndorder'),
    path('catagory/subcatagory/<str:pk>', views.subcatagory, name='subcatagory'),
    path('catagory/subcatagory/<str:pk>/products/<str:pk1>', views.products, name='products'),
    path('catagory/subcatagory/<str:pk>/products/<str:pk1>/productdetails/<str:pk2>', views.productdetails, name='productdetails'),
]



from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    # path('login/', views.login_page, name='login_page'),
    # path('register/', views.register_page, name='register_page'),
    path("logout/", LogoutView.as_view(), name="user_logout"),


]

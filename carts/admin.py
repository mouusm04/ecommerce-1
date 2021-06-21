from django.contrib import admin

# Register your models here.
from .models import Cart, OrderItem
# Register your models here.
admin.site.register(Cart)
admin.site.register(OrderItem)

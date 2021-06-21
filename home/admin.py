from django.contrib import admin

from .models import Product, Catagory, SubCatagory
# Register your models here.
admin.site.register(Product)
admin.site.register(SubCatagory)
admin.site.register(Catagory)

from django.shortcuts import render, redirect
from .models import Cart, OrderItem
from django.http import JsonResponse
from home.models import Product
# Create your views here.
from postaladdress.forms import AddressForm
from billing.models import BillingProfile
from orders.models import Order
from postaladdress.models import Address
import json


def cart_deatil_api_view(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = [{
        "id":x.id,
        "title":x.title,
        "price":x.price,
        "image":x.image.url,
        
    }
        for x in cart_obj.products.all()]
    cart_data = {
        "products": products,
        "subtotal": cart_obj.subtotal,
        "total" : cart_obj.total,
    }    
    return JsonResponse(cart_data)


def cart_home(request):
    cart, cart_created = Cart.objects.new_or_get(request)
    print(cart)
    items=cart.orderitem_set.all()
    print(items)
    context = {
        "cart":cart,
        "items":items

    }

    return render(request, "carts/home.html", context)



def cart_update(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action:', action)
    print('productId:', productId)

    product = Product.objects.get(id=productId)
    cart, cart_created = Cart.objects.new_or_get(request)
    orderitem, orderitem_created = OrderItem.objects.get_or_create(product=product, cart=cart, user=request.user)

    cart = Cart.objects.get()
    if action =='add':
        cart.products.add(product)
    elif action =='remove':
        cart.products.remove(product)
    cart.save()    

    if action =='additem':
        orderitem.quantity = (orderitem.quantity + 1)
    elif action == 'removeitem':
        orderitem.quantity = (orderitem.quantity - 1)  

    orderitem.save()

    if orderitem.quantity <=0 or action == 'remove':
        orderitem.delete() 
        cart.products.remove(product)

    request.session['cart_items'] = cart.get_cart_item_total        
    return JsonResponse('Item was added', safe=False)


def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj =None
    if cart_created or cart_obj.products.count()==0:
        return redirect ("cart_home")
    items=cart_obj.orderitem_set.all()
    address_form = AddressForm()
    billing_address_form = AddressForm()
    shipping_address_id = request.session.get("shipping_address_id", None)

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    if billing_profile is not None:
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
        if shipping_address_id:
            order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
            del request.session["shipping_address_id"]
            order_obj.save()

    context = {
        "object" : order_obj,
        "items":items,
        'billing_profile' : billing_profile,
        'address_form' : address_form,
        'billing_address_form': billing_address_form

    }         



    return render(request, "carts/checkout.html", context)


def payment(request):
    cart = Cart.objects.all()
    context = {
        'cart':cart
    }
    return render(request, "carts/payment.html", context)    

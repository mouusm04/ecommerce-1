from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Product, Catagory, SubCatagory
from carts.models import Cart
from carts.forms import sizeForm
from carts.models import OrderItem
from orders.models import Order
from billing.models import BillingProfile

from .forms import ContactForm, LoginForm, RegisterForm

def home(request):
   
    context = {
        
    }
    return render(request, 'home/home.html', context)


def catagory(request):
    catagories = Catagory.objects.all()
    # print(catagories)
    context = {
        'catagories':catagories
        } 
    return render(request, 'home/catagory.html', context)


def subcatagory(request, pk):
    catagory = Catagory.objects.get(id=pk)
    subcatagories = catagory.subcatagory_set.all()
    context = {
        'subcatagories' : subcatagories
    } 
    return render(request, 'home/subcatagory.html', context)

def products(request, pk, pk1):
    subcatagory = SubCatagory.objects.get(id=pk1)
    products = subcatagory.product_set.all()
    context = {
        'products' : products,
    }    

    return render(request, 'home/product.html', context) 

@login_required(login_url='/register/')
def productdetails(request, pk, pk1, pk2):

    cart, cart_created = Cart.objects.new_or_get(request)
    product = Product.objects.get(id=pk2)
    form =sizeForm(instance=product)
    if request.method =='POST':
        form = sizeForm(request.POST, instance =product)
        if form.is_valid():
            quantity=form.cleaned_data.get('quantity')
            print(quantity)
            orderitem, orderitem_created = OrderItem.objects.get_or_create(product=product, cart=cart, user=request.user, quantity=quantity)
 

            

    context= {
        'object' : product,
        'form':form
    }
    return render(request, 'home/productdetails.html', context)



def about_page(request):
    context = {
        "title": "Welcome to aboutpage"
    }
    return render(request, 'home/home_page.html', context)


def logout(request):
    context = {
        "title": "Welcome to aboutpage"
    }
    return redirect("login_page")      
    
def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Welcome to contact page",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if request.method == "POST":
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, 'home/contact.html', context)    

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    } 
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")


        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # context['form'] = LoginForm()
            return redirect("catagory")
        else:
            print("error")
    return render(request, "accounts/login.html", context)    

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        
    return render(request, "accounts/register.html", context)       


def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', False)
        print(searched)
        products = Product.objects.all().filter(title__contains=searched)
        print(products)
        context = {
            'products': products,
            'searched':searched
        }

    return render(request, 'home/search.html', context)


def returnAndorder(request):
    context = {}
    return render(request, "home/return.html", context)






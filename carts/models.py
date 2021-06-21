from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed

from home.models import Product


User= settings.AUTH_USER_MODEL

class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() ==1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)   
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj



    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)       

class Cart(models.Model):
 
    user     = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    subtotal = models.DecimalField(default = 0.00, max_digits=100, decimal_places=2)
    total    = models.DecimalField(default = 0.00, max_digits=100, decimal_places=2)
    updated  = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

    @property    
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_item(self):
        orderitems = self.orderitem_set.all()
        subtotal = sum([item.quantity for item in orderitems])
        return subtotal    
    @property
    def get_final_total(self):
        final_total = self.get_cart_total
        total = final_total + 10
        return total  
    @property
    def get_cart_item_total(self):
        orderitems = OrderItem.objects.all().count()
        return orderitems



class OrderItem(models.Model):

    user     = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True, verbose_name = "Qty ",)
    date_added = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total



def m2m_changed_card_receiver(sender, instance, action, *args, **kwargs):
    if action =='post_add' or action =='post_remove' or action =='post_clear':
        products = instance.products.all()
        total = 0
        for x in products:
            total += x.price
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()    

m2m_changed.connect(m2m_changed_card_receiver, sender = Cart.products.through)


def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    instance.total = instance.subtotal +10

pre_save.connect(pre_save_cart_receiver, sender=Cart)

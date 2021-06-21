from django.db import models
from billing.models import BillingProfile
# Create your models here.


Address_types = (
    ('billing', 'Billing address'),
    ('shipping', 'Shipping address'),
)

class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=True, blank=True, help_text='Shipping to? Who is it for?')
    address_line_1  = models.CharField(max_length=120)
    address_line_2  = models.CharField(max_length=120, null=True, blank=True)
    address_type    = models.CharField(max_length=120, choices=Address_types, default='Shipping address')
    city            = models.CharField(max_length=120)
    country         = models.CharField(max_length=120)
    state           = models.CharField(max_length=120)
    postal_code     = models.CharField(max_length=120)

    def __str__(self):
        return str(self.billing_profile)

    def get_address(self):
            return "{line1}\n{line2}\n{city}\n{state}, {postal}\n{country}".format(
            
            line1 = self.address_line_1,
            line2 = self.address_line_2 or "",
            city = self.city,
            state = self.state,
            postal= self.postal_code,
            country = self.country
        )    

    def get_city(self):
            return "{city}\n{postal}".format(
     
            city = self.city,
            postal= self.postal_code,
       
        )    

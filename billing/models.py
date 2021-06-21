from django.db import models
from django.conf import settings
from django.db.models.signals import post_save, pre_save

User = settings.AUTH_USER_MODEL

class BillingProfileManager(models.Manager):
    def new_or_get(self, request):
        user=request.user
        created = False
        obj =None
        if user.is_authenticated:
            obj, created = self.model.objects.get_or_create(user=user, email=user.email)

        else:
            pass
        return obj, created

class BillingProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email= models.EmailField()
    active=models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    customer_id=models.CharField(max_length=120, null=True, blank=True)

    objects = BillingProfileManager()

    def __str__(self):
        return self.email

def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created:
        BillingProfile.objects.create(user=instance)



post_save.connect(user_created_receiver, sender=User)

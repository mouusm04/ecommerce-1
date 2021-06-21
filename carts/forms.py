from django import forms
from .models import OrderItem



class sizeForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']
